# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
