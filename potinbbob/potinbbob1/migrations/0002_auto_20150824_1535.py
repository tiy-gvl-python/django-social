# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potinbbob1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('genre', models.TextField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pic',
            name='tag',
            field=models.ManyToManyField(to='potinbbob1.Genre'),
        ),
    ]
