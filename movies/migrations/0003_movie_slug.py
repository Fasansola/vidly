# Generated by Django 5.0.5 on 2024-05-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
