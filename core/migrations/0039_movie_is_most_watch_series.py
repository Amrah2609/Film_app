# Generated by Django 5.2.3 on 2025-07-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0038_movie_is_rated_scenes"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="is_most_watch_series",
            field=models.BooleanField(default=False),
        ),
    ]
