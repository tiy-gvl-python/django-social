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
            name='Friendship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('circle', models.CharField(max_length=50)),
                ('creation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=1, blank=True)),
                ('birthday', models.DateField(null=True)),
                ('creation', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now=True)),
                ('guser', models.ForeignKey(to='social.Guser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('data', models.CharField(max_length=1000)),
                ('public', models.BooleanField(default=True)),
                ('creation', models.DateTimeField(auto_now=True)),
                ('guser', models.ForeignKey(to='social.Guser')),
                ('parent_post', models.ForeignKey(null=True, to='social.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostCircle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now=True)),
                ('circle', models.ForeignKey(to='social.Friendship')),
                ('post', models.ForeignKey(to='social.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_now=True)),
                ('guser', models.ForeignKey(to='social.Guser', related_name='tag_guser')),
                ('post', models.ForeignKey(to='social.Post')),
                ('tagger', models.ForeignKey(to='social.Guser', related_name='tag_tagger')),
            ],
        ),
        migrations.AddField(
            model_name='plus',
            name='post',
            field=models.ForeignKey(to='social.Post'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(to='social.Guser', related_name='friendship_friend'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='guser',
            field=models.ForeignKey(to='social.Guser', related_name='friendship_guser'),
        ),
    ]
