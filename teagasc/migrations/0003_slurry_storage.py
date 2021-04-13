# Generated by Django 3.1.2 on 2021-04-08 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teagasc', '0002_delete_slurry_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slurry_Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField(null=True)),
                ('breadth', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('zone', models.IntegerField(null=True)),
                ('total_slurry_manure', models.FloatField(null=True)),
                ('total_storage', models.FloatField(null=True)),
                ('rainfall', models.FloatField(null=True)),
                ('farmer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teagasc.farmer')),
            ],
        ),
    ]
