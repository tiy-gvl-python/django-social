# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('subscriptions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subscribers', models.ForeignKey(to='mines_app.Subscribe')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('bool', models.BooleanField()),
                ('posts', models.ForeignKey(to='mines_app.Post')),
            ],
        ),
        migrations.AddField(
            model_name='subscribe',
            name='to',
            field=models.ForeignKey(to='mines_app.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='mines_app.User'),
        ),
    ]
