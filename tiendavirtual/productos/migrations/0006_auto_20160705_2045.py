# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20160705_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=4),
        ),
    ]
