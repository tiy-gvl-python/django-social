# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#raise Exception()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('comment', models.CharField(max_length=60)),
                ('user', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comment', models.CharField(max_length=60)),
                ('time_date', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=25)),
                ('link_to_origin', models.CharField(max_length=150)),
                ('origin_info', models.CharField(max_length=35)),
                ('humor', models.BooleanField(default=False)),
                ('instructional', models.BooleanField(default=False)),
                ('sappy', models.BooleanField(default=False)),
                ('sad', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('full_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=25)),
                ('website', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]
