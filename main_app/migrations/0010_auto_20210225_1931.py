# Generated by Django 3.1.7 on 2021-02-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210225_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='waterAmount',
            new_name='water_amount',
        ),
    ]
