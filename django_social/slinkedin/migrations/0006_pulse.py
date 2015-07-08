# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slinkedin', '0005_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pulse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('articles', models.TextField()),
                ('like', models.BooleanField()),
                ('comment', models.TextField()),
                ('recommendation', models.ForeignKey(to='slinkedin.User')),
            ],
        ),
    ]
