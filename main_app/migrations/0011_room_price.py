# Generated by Django 4.2.5 on 2023-09-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_excursion_picturepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=''),
        ),
    ]
