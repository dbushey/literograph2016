# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-08 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lito', '0010_auto_20160507_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypoint',
            name='num_order',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]