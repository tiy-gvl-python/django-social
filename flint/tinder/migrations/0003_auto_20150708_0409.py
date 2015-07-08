# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0002_auto_20150708_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferrence',
            name='preferred_id',
            field=models.ForeignKey(related_name='swiped', to='tinder.Profile'),
        ),
        migrations.AlterField(
            model_name='preferrence',
            name='primary_id',
            field=models.ForeignKey(related_name='swiper', to='tinder.Profile'),
        ),
    ]
