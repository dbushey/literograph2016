# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lito', '0011_storypoint_num_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypoint',
            name='num_order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
