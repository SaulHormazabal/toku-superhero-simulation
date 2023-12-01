import random

from simulation.config.celery import app
from simulation.apps.characters.models import Character, CharacterAlignment

from .models import Fight


def choose_random_hero(alignment: str):
    """Chooses a random hero from the SuperHero API."""

    characters = Character.objects.filter(
        alignment__name=alignment,
        hp__isnull=False,
        attack__isnull=False,
    )

    return characters.order_by('?').first()


@app.task
def simulate_fight(fight_id):
    """Simulates a fight between two heroes."""

    hero = choose_random_hero(CharacterAlignment.Names.GOOD)
    villain = choose_random_hero(CharacterAlignment.Names.BAD)

    hero.hp_current = hero.hp
    villain.hp_current = villain.hp

    fight = Fight.objects.get(id=fight_id)

    is_hero_turn = random.choice([True, False])

    while fight.winner is None:
        fight.turns += 1

        if is_hero_turn:
            villain.hp_current -= hero.attack

            if villain.hp_current <= 0:
                fight.winner = hero
                fight.loser = villain

        else:
            hero.hp_current -= villain.attack

            if hero.hp_current <= 0:
                fight.winner = villain
                fight.loser = hero

        is_hero_turn = not is_hero_turn

    fight.save()

    return {
        'winner': fight.winner_id,
        'loser': fight.loser_id,
        'turns': fight.turns,
    }
