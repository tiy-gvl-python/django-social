# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mines_app', '0002_remove_subscribe_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', models.TextField(max_length=50)),
                ('related_comments', models.ForeignKey(to='mines_app.Post')),
                ('related_votes', models.ForeignKey(to='mines_app.Vote')),
                ('user', models.ForeignKey(to='mines_app.User')),
            ],
        ),
    ]
