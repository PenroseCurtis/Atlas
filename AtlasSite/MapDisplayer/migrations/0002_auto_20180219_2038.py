# Generated by Django 2.0.2 on 2018-02-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MapDisplayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kingdom',
            name='name',
            field=models.CharField(default='ni', max_length=100),
        ),
        migrations.AddField(
            model_name='map',
            name='imageURL',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='map',
            name='name',
            field=models.CharField(default='ni', max_length=100),
        ),
    ]