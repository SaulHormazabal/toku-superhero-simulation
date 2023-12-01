from django.db import models
from django_pgviews import view as pg

from simulation.apps.characters.models import Character, CharacterAlignment


CHARACTER_STATISTICS_SQL = '''
    SELECT
        c.id AS id,
        c.id AS character_id,
        c.name AS character_name,
        COUNT(f.id) AS total_fights,
        COUNT(f.winner_id) AS wins,
        COUNT(f.loser_id) AS losses,
        COALESCE(COUNT(f.winner_id) / NULLIF(COUNT(f.id), 0), 0) AS win_rate
    FROM
        characters_character c
    LEFT JOIN
        fights_fight f ON c.id = f.winner_id OR c.id = f.loser_id
    GROUP BY
        c.id, c.name;
'''


ALIGNMENT_STATISTICS_SQL = '''
    SELECT
        ca.id AS id,
        ca.id AS alignment_id,
        ca.name AS alignment_name,
        COUNT(f.id) AS total_fights,
        COUNT(f.winner_id) AS wins,
        COUNT(f.loser_id) AS losses,
        COALESCE(COUNT(f.winner_id) / NULLIF(COUNT(f.id), 0), 0) AS win_rate
    FROM
        characters_characteralignment ca
    LEFT JOIN
        characters_character c ON ca.id = c.alignment_id
    LEFT JOIN
        fights_fight f ON c.id = f.winner_id OR c.id = f.loser_id
    GROUP BY
        ca.id, ca.name;
'''


class CharacterStatistics(pg.View):

    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        related_name='statistics',
    )

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    win_rate = models.FloatField(default=0.0)
    total_fights = models.IntegerField(default=0)

    sql = CHARACTER_STATISTICS_SQL

    class Meta:
        managed = False


class AlignmentStatistics(pg.View):

    alignment = models.OneToOneField(
        CharacterAlignment,
        on_delete=models.CASCADE,
        related_name='statistics',
    )

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    win_rate = models.FloatField(default=0.0)
    total_fights = models.IntegerField(default=0)

    sql = ALIGNMENT_STATISTICS_SQL

    class Meta:
        managed = False
