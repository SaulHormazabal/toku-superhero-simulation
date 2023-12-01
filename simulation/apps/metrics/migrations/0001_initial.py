# Generated by Django 4.2.7 on 2023-11-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AlignmentStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wins", models.IntegerField(default=0)),
                ("losses", models.IntegerField(default=0)),
                ("win_rate", models.FloatField(default=0.0)),
                ("total_fights", models.IntegerField(default=0)),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CharacterStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wins", models.IntegerField(default=0)),
                ("losses", models.IntegerField(default=0)),
                ("win_rate", models.FloatField(default=0.0)),
                ("total_fights", models.IntegerField(default=0)),
            ],
            options={
                "managed": False,
            },
        ),
    ]
