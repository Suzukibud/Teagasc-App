# Generated by Django 3.1.2 on 2021-04-05 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teagasc', '0029_remove_exportation_farmer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportation',
            name='farmer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teagasc.farmer'),
        ),
    ]
