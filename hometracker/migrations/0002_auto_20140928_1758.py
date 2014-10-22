# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='xcoordinate',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='ycoordinate',
            field=models.FloatField(blank=True),
        ),
    ]
