# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_type', models.CharField(max_length=255)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=255)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Airplane')),
            ],
        ),
        migrations.CreateModel(
            name='TravelClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_class_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TravelClassSeatCapacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_capacity', models.IntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Flight')),
                ('travel_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.TravelClass')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='travel_class',
            field=models.ManyToManyField(through='airline.TravelClassSeatCapacity', to='airline.TravelClass'),
        ),
    ]
