# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("CASH", "cash"),
                            ("CHEQUE", "cheque"),
                            ("VOLUNTEERING", "volunteering"),
                            ("STRIPE", "stripe"),
                            ("PAYPAL", "paypal"),
                        ],
                        max_length=12,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "membership",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Membership",
                    ),
                ),
            ],
        ),
    ]
