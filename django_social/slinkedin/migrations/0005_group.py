# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slinkedin', '0004_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('discussion', models.CharField(max_length=100)),
                ('members', models.CharField(max_length=100)),
                ('group', models.ForeignKey(to='slinkedin.Company')),
            ],
        ),
    ]
