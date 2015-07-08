# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0003_auto_20150708_0409'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preferrence',
            new_name='Preference',
        ),
    ]
