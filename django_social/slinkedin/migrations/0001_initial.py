# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('employment', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('experience', models.TextField()),
                ('skills', models.TextField()),
                ('messages', models.TextField()),
                ('posts', models.TextField()),
                ('invitations', models.CharField(max_length=100)),
            ],
        ),
    ]
