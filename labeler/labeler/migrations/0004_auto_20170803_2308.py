# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeler', '0003_auto_20170803_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='uploaded_date',
        ),
        migrations.AddField(
            model_name='image',
            name='taken_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='Date photo was taken.'),
        ),
        migrations.AddField(
            model_name='image',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Date photo was changed.'),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date photo was uploaded.'),
        ),
    ]
