# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-25 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0006_auto_20180723_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='groupid',
        ),
    ]