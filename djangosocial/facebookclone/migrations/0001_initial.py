# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateField(auto_now=True)),
                ('friend', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friend')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='CUser')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('message', models.TextField()),
                ('pub_date', models.DateField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, to='facebookclone.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateField(auto_now=True)),
                ('status', models.ForeignKey(to='facebookclone.Status')),
                ('tagged', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='Tagged')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='Tagger')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(to='facebookclone.Status'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
