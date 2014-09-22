# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hometracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mlsid', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('askingprice', models.IntegerField()),
                ('offeredpricce', models.IntegerField()),
                ('soldprice', models.IntegerField()),
                ('numofbdrms', models.IntegerField()),
                ('numofbthrms', models.FloatField()),
                ('numofmaster', models.IntegerField()),
                ('frontyard', models.BooleanField(default=False)),
                ('backyard', models.BooleanField(default=False)),
                ('propertytype', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roof', models.CharField(max_length=100)),
                ('kitchen', models.CharField(max_length=100)),
                ('bathrooms', models.CharField(max_length=100)),
                ('frontyard', models.CharField(max_length=100)),
                ('backyard', models.CharField(max_length=100)),
                ('termite', models.CharField(max_length=100)),
                ('foundation', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('property', models.ForeignKey(related_name=b'propertynotes', to='hometracker.Property')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shopper',
            name='property',
            field=models.ManyToManyField(related_name=b'property', to='hometracker.Property'),
            preserve_default=True,
        ),
    ]
