# Generated by Django 5.2.3 on 2025-07-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0037_remove_movie_is_web_series_background_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="is_rated_scenes",
            field=models.BooleanField(default=False),
        ),
    ]
