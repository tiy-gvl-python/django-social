# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Queried',
            new_name='Preferrence',
        ),
        migrations.AlterModelOptions(
            name='preferrence',
            options={'ordering': ['primary_id']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
