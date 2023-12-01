from django.db import models

from simulation.apps.characters.models import Character


class Fight(models.Model):

    id = models.IntegerField(primary_key=True)

    winner = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, related_name='wins')
    loser = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, related_name='losses')

    turns = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
