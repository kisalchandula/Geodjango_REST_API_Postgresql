# Generated by Django 3.2.7 on 2021-10-01 14:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pokemoncenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('master', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
    ]
