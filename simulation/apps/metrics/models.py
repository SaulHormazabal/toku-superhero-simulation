from django.db import models
from django_pgviews import view as pg

from simulation.apps.characters.models import Character, CharacterAlignment


CHARACTER_STATISTICS_SQL = '''
    SELECT
        c.id AS id,
        c.id AS character_id,
        c.name AS character_name,
        COALESCE(COUNT(DISTINCT ff_winner.id), 0) AS wins,
        COALESCE(COUNT(DISTINCT ff_loser.id), 0) AS losses,
        COALESCE(COUNT(DISTINCT ff.id), 0) AS total_fights,
        COALESCE(
            (COUNT(DISTINCT ff_winner.id)::float / NULLIF(COUNT(DISTINCT ff.id), 0)) * 100, 0
        ) AS win_rate
    FROM
        public.characters_character c
    LEFT JOIN
        public.fights_fight ff_winner ON c.id = ff_winner.winner_id
    LEFT JOIN
        public.fights_fight ff_loser ON c.id = ff_loser.loser_id
    LEFT JOIN
        public.fights_fight ff ON c.id = ff.winner_id OR c.id = ff.loser_id
    GROUP BY
        c.id, c.name;
'''


ALIGNMENT_STATISTICS_SQL = '''
    SELECT
        ca.id AS id,
        ca.id AS alignment_id,
        ca.name AS alignment_name,
        COALESCE(COUNT(DISTINCT ff_winner.id), 0) AS wins,
        COALESCE(COUNT(DISTINCT ff_loser.id), 0) AS losses,
        COALESCE(COUNT(DISTINCT ff.id), 0) AS total_fights,
        COALESCE(
            COUNT(DISTINCT ff_winner.id)::float / NULLIF(COUNT(DISTINCT ff.id), 0) * 100, 0
        ) AS win_rate
    FROM
        public.characters_characteralignment ca
    LEFT JOIN
        public.characters_character c ON ca.id = c.alignment_id
    LEFT JOIN
        public.fights_fight ff_winner ON c.id = ff_winner.winner_id
    LEFT JOIN
        public.fights_fight ff_loser ON c.id = ff_loser.loser_id
    LEFT JOIN
        public.fights_fight ff ON c.id = ff.winner_id OR c.id = ff.loser_id
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
