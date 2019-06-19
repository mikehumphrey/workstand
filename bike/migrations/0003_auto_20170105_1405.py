# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_auto_20170105_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='size',
            field=models.TextField(blank=True, choices=[('C', 'child'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large')], max_length=2, null=True),
        ),
    ]