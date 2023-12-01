import requests

from django.conf import settings

from simulation.config.celery import app

from .models import Character, CharacterAlignment


def float_or_none(value):
    return None if value == "null" else float(value)


@app.task
def sync_characters(api_id: int, sync_next_id: bool = False):

    created = False
    detail = None
    add_next_task = sync_next_id

    url = f'{settings.SUPERHERO_API_URL}/{api_id}'
    response = requests.get(url, timeout=5)
    result = response.json()

    if response.status_code == 404:
        detail = f'Character {api_id} was not found, stopping sync.'
        add_next_task = False

    if result['response'] == 'error':
        detail = f'Character {api_id} returned an error, stopping sync.'
        add_next_task = False

    if response.status_code == 200 and result['response'] == 'success':

        alignment, _ = CharacterAlignment.objects.get_or_create(
            name=result['biography']['alignment'],
        )

        stats = result['powerstats']

        character, created = Character.objects.update_or_create(
            api_id=api_id,
            defaults={
                'name': result['name'],
                'intelligence': float_or_none(stats['intelligence']),
                'strength': float_or_none(stats['strength']),
                'speed': float_or_none(stats['speed']),
                'durability': float_or_none(stats['durability']),
                'power': float_or_none(stats['power']),
                'combat': float_or_none(stats['combat']),
                'alignment': alignment,
            },
        )

        character.calc_hp()
        character.calc_attack()

        character.save()

        detail = f"Character {character.name} was synchronized."

    if add_next_task:
        sync_characters.delay(api_id=api_id + 1, sync_next_id=True)

    return {
        'created': created,
        'detail': detail,
        'added_next_task': add_next_task,
    }
