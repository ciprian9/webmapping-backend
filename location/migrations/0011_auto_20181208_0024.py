# Generated by Django 2.1.2 on 2018-12-08 00:24

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_auto_20181207_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarBucks',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='number')),
                ('street', models.CharField(max_length=200, verbose_name='name')),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='position')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='dublinbikes',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 0, 24, 15, 729306, tzinfo=utc)),
        ),
    ]