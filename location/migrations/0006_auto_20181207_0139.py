# Generated by Django 2.1.2 on 2018-12-07 01:39

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20181207_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dublinbikes',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='position'),
        ),
    ]
