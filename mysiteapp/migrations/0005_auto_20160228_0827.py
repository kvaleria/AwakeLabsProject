# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-26 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysiteapp', '0004_auto_20160228_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysiteapp.Event'),
        ),
    ]
