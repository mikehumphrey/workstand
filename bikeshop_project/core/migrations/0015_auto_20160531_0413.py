# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_payment_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('CASH', 'cash'), ('CHEQUE', 'cheque'), ('VOLUNTEERING', 'volunteering'), ('STRIPE', 'stripe'), ('PAYPAL', 'paypal')], default='None', max_length=12),
        ),
    ]
