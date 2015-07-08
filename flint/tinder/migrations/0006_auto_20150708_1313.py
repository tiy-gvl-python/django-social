# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0005_comment_moment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moment',
            name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='temp',
            new_name='moment',
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Moment',
        ),
    ]
