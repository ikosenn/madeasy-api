# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-13 16:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParserResults',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('query', models.CharField(max_length=255)),
                ('parser_time', models.FloatField(default=0.0, help_text='The time it takes the parser to understand the query')),
                ('response_time', models.FloatField(default=0.0, help_text='The time it takes from querying to fetching a result')),
                ('is_correct', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
