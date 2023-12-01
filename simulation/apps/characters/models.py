from django.db import models


class CharacterAlignment(models.Model):

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Names(models.TextChoices):
        GOOD = 'good'
        BAD = 'bad'
        NEUTRAL = 'neutral'

    def __str__(self):
        return self.name


class Character(models.Model):

    api_id = models.IntegerField()
    name = models.CharField(max_length=255)

    intelligence = models.FloatField(null=True)
    strength = models.FloatField(null=True)
    speed = models.FloatField(null=True)
    durability = models.FloatField(null=True)
    power = models.FloatField(null=True)
    combat = models.FloatField(null=True)

    hp = models.FloatField(null=True)
    attack = models.FloatField(null=True)

    alignment = models.ForeignKey(
        CharacterAlignment,
        on_delete=models.CASCADE,
        related_name='characters',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def calc_hp(self):
        """Calculates the HP of a hero."""
        try:
            hero_hp = self.strength + self.durability + self.combat / 2

        except TypeError:
            hero_hp = None

        self.hp = hero_hp

    def calc_attack(self):
        """Calculates the attack of a hero."""

        try:
            if self.alignment.name == CharacterAlignment.Names.GOOD:
                hero_attack = self.calc_good_hero_attack()

            elif self.alignment.name == CharacterAlignment.Names.BAD:
                hero_attack = self.calc_bad_hero_attack()

            else:
                hero_attack = self.strength + self.power + self.combat / 2

        except TypeError:
            hero_attack = None

        self.attack = hero_attack

    def calc_good_hero_attack(self):
        """Calculates the attack of the good hero."""
        attack = ((self.strength + self.power) / 4) * ((self.intelligence + self.speed) / 3) / 10

        return attack

    def calc_bad_hero_attack(self):
        """Calculates the attack of the good hero."""
        attack = ((self.strength + self.power) / 3) * ((self.intelligence + self.speed) / 4) / 10

        return attack
