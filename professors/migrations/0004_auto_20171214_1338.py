# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-14 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0003_auto_20171214_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='lastnames',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='names',
        ),
    ]