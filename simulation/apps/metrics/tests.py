from django.test import TestCase
from django.db import connection

from simulation.apps.characters.models import Character, CharacterAlignment
from simulation.apps.fights.models import Fight

from .models import AlignmentStatistics, CharacterStatistics


class MetricsTest(TestCase):

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

        self.fight = Fight.objects.create(id=1, turns=1, winner=self.villain, loser=self.hero)
        self.fight = Fight.objects.create(id=2, turns=1, winner=self.hero, loser=self.villain)
        self.fight = Fight.objects.create(id=3, turns=1, winner=self.hero, loser=self.villain)
        self.fight = Fight.objects.create(id=4, turns=1, winner=self.hero, loser=self.villain)

        self.alignment_expected = {
            'good': {
                'wins': 3,
                'losses': 1,
                'win_rate': 75.0,
            },
            'bad': {
                'wins': 1,
                'losses': 3,
                'win_rate': 25.0,
            },
        }

        self.character_expected = {
            self.hero.id: self.alignment_expected['good'],
            self.villain.id: self.alignment_expected['bad'],
        }

    def test_alignment_metrics(self):
        sql = AlignmentStatistics.sql
        query = CharacterAlignment.objects.raw(sql)

        for alignment in query:
            expected = self.alignment_expected[alignment.name]

            self.assertEqual(alignment.wins, expected['wins'])
            self.assertEqual(alignment.losses, expected['losses'])
            self.assertEqual(alignment.win_rate, expected['win_rate'])

    def test_character_metrics(self):
        sql = CharacterStatistics.sql

        with connection.cursor() as cursor:
            cursor.execute(sql)

            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        for character in results:
            expected = self.character_expected[character['character_id']]

            self.assertEqual(character['wins'], expected['wins'])
            self.assertEqual(character['losses'], expected['losses'])
            self.assertEqual(character['win_rate'], expected['win_rate'])
