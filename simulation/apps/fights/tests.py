from django.test import TestCase

from simulation.apps.characters.models import Character, CharacterAlignment

from .models import Fight
from .tasks import simulate_fight, choose_random_hero


class FightSimulationTestCase(TestCase):
    def setUp(self):
        self.hero_alignment = CharacterAlignment.objects.create(
            name=CharacterAlignment.Names.GOOD,
        )
        self.villain_alignment = CharacterAlignment.objects.create(
            name=CharacterAlignment.Names.BAD,
        )

        self.hero = Character.objects.create(
            api_id=1,
            name="SuperHero",
            alignment=self.hero_alignment,
            hp=100,
            attack=20,
        )

        self.villain = Character.objects.create(
            api_id=2,
            name="EvilVillain",
            alignment=self.villain_alignment,
            hp=80,
            attack=25,
        )

        self.fight = Fight.objects.create(id=1)

    def test_choose_random_hero(self):
        hero = choose_random_hero(CharacterAlignment.Names.GOOD)
        self.assertIsNotNone(hero)

    def test_simulate_fight(self):
        simulate_fight(self.fight.id)

        self.fight.refresh_from_db()

        self.assertIsNotNone(self.fight.winner)
        self.assertIsNotNone(self.fight.loser)

        self.assertGreater(self.fight.turns, 0)
