# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0004_auto_20150708_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('temp', models.BooleanField()),
                ('profile', models.ForeignKey(to='tinder.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(to='tinder.Comment')),
            ],
        ),
    ]
