# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-18 09:16
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madeasy_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='actions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
    ]
