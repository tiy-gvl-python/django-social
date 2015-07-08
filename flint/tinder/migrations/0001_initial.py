# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=200)),
                ('distance', models.IntegerField(default=1)),
                ('age', models.IntegerField(default=18)),
                ('sex', models.BooleanField()),
                ('preferred_sex', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Queried',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('primary_id', models.IntegerField(default=None)),
                ('preferred_id', models.IntegerField(default=None)),
                ('preferrence', models.BooleanField()),
            ],
        ),
    ]
