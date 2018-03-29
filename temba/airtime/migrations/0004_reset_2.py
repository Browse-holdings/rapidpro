# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 22:38
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airtime', '0003_reset_1'),
        ('channels', '0050_reset_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='airtimetransfer',
            name='channel',
            field=models.ForeignKey(blank=True, help_text='The channel that this airtime is relating to', null=True, on_delete=django.db.models.deletion.CASCADE, to='channels.Channel'),
        ),
    ]