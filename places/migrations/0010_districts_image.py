# Generated by Django 4.0.2 on 2022-02-19 17:20

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_districts_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='image',
            field=models.ImageField(default='', upload_to=places.models.Districts.nameFile),
        ),
    ]
