# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometracker', '0002_auto_20140928_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='xcoordinate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='ycoordinate',
            field=models.FloatField(null=True),
        ),
    ]
