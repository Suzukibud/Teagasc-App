# Generated by Django 3.1.2 on 2021-01-12 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teagasc', '0004_auto_20201217_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmer',
            old_name='land',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='farmer',
            old_name='year',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='type_of_stock',
        ),
    ]
