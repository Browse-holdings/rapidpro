# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0138_flowrun_current_node_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowstep',
            name='step_uuid',
            field=models.CharField(help_text='The UUID of the ActionSet or RuleSet for this step', max_length=36),
        ),
    ]
