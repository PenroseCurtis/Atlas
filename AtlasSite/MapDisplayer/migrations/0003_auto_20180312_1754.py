# Generated by Django 2.0.2 on 2018-03-12 17:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MapDisplayer', '0002_auto_20180219_2038'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kingdom',
            new_name='Region',
        ),
        migrations.AddField(
            model_name='map',
            name='full_link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='map',
            name='indices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=list, size=None),
        ),
        migrations.AddField(
            model_name='map',
            name='parentMap',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MapDisplayer.Map'),
        ),
        migrations.AddField(
            model_name='map',
            name='summary',
            field=models.CharField(default='', max_length=500),
        ),
    ]
