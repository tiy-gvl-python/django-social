# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slinkedin', '0006_pulse'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('school_ranking', models.IntegerField()),
                ('field_of_study', models.CharField(max_length=100)),
                ('employment', models.CharField(max_length=100)),
                ('education', models.ForeignKey(to='slinkedin.User')),
            ],
        ),
    ]
