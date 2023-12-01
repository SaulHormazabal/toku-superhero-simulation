# Generated by Django 4.2.7 on 2023-11-30 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CharacterAlignment",
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
                ("name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Character",
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
                ("api_id", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("intelligence", models.FloatField()),
                ("strength", models.FloatField()),
                ("speed", models.FloatField()),
                ("durability", models.FloatField()),
                ("power", models.FloatField()),
                ("combat", models.FloatField()),
                ("hp", models.FloatField()),
                ("attack", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "alignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="characters",
                        to="characters.characteralignment",
                    ),
                ),
            ],
        ),
    ]
