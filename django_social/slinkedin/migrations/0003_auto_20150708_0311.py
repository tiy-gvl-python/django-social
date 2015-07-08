# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slinkedin', '0002_connection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('post_job', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='invitations',
            new_name='invitation',
        ),
        migrations.AddField(
            model_name='job',
            name='jobs',
            field=models.ForeignKey(to='slinkedin.User'),
        ),
    ]
