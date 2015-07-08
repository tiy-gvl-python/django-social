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
            name='CommonUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('topic', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('genre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('instrument', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('video', models.CharField(max_length=300)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('genre', models.ManyToManyField(to='social_network.Genre')),
                ('instrument', models.ManyToManyField(to='social_network.Instrument')),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('commonuser_ptr', models.OneToOneField(to='social_network.CommonUser', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('genre', models.ManyToManyField(to='social_network.Genre')),
                ('instrument', models.ManyToManyField(to='social_network.Instrument')),
            ],
            bases=('social_network.commonuser',),
        ),
        migrations.AddField(
            model_name='commonuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='musician',
            field=models.OneToOneField(to='social_network.Musician'),
        ),
    ]
