# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometracker', '0003_auto_20140928_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='prop_image',
            field=models.ImageField(default=2014, upload_to=b'prop_image', blank=True),
            preserve_default=False,
        ),
    ]
