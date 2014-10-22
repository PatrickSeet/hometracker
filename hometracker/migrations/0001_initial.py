# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(help_text=b'Format should be: 650-111-2222', max_length=12)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mlsid', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('numofbdrms', models.IntegerField()),
                ('numofbthrms', models.FloatField()),
                ('numofmaster', models.IntegerField()),
                ('sqfootage', models.IntegerField()),
                ('lotsize', models.IntegerField()),
                ('askingprice', models.IntegerField()),
                ('offeredpricce', models.IntegerField()),
                ('soldprice', models.IntegerField()),
                ('frontyard', models.BooleanField(default=False)),
                ('backyard', models.BooleanField(default=False)),
                ('propertytype', models.CharField(max_length=100)),
                ('xcoordinate', models.FloatField()),
                ('ycoordinate', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyNotes',
            fields=[
                ('roof', models.CharField(max_length=100)),
                ('kitchen', models.CharField(max_length=100)),
                ('bathrooms', models.CharField(max_length=100)),
                ('frontyard', models.CharField(max_length=100)),
                ('backyard', models.CharField(max_length=100)),
                ('termite', models.CharField(max_length=100)),
                ('foundation', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('property', models.OneToOneField(primary_key=True, serialize=False, to='hometracker.Property')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='property',
            name='shopper',
            field=models.ForeignKey(related_name=b'shopper', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
