# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-26 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysiteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysiteapp.Event'),
        ),
    ]
