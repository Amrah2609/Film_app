# Generated by Django 5.2.3 on 2025-07-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0032_movie_background_image_ppoi_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="background_image_ppoi",
        ),
        migrations.AlterField(
            model_name="movie",
            name="background_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
