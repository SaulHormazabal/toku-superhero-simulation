from django.test import TestCase

from .models import Character, CharacterAlignment


class CharacterModelTest(TestCase):
    def setUp(self):
        self.alignment = CharacterAlignment.objects.create(name=CharacterAlignment.Names.GOOD)

        self.hero = Character.objects.create(
            api_id=1,
            name="SuperHero",
            alignment=self.alignment,
            intelligence=63,
            strength=80,
            speed=23,
            durability=90,
            power=100,
            combat=32,
        )

        self.villain = Character.objects.create(
            api_id=2,
            name="EvilVillain",
            alignment=self.alignment,
            intelligence=50,
            strength=80,
            speed=42,
            durability=90,
            power=100,
            combat=50,
        )

    def test_calc_hp(self):
        self.assertIsNone(self.hero.hp)
        self.hero.calc_hp()
        self.assertIsNotNone(self.hero.hp)

    def test_calc_attack(self):
        self.assertIsNone(self.hero.attack)
        self.hero.calc_attack()
        self.assertIsNotNone(self.hero.attack)

    def test_calc_good_hero_attack(self):
        attack = self.hero.calc_good_hero_attack()
        self.assertEqual(attack, 129)

    def test_calc_bad_hero_attack(self):
        attack = self.villain.calc_bad_hero_attack()
        self.assertEqual(attack, 138)
