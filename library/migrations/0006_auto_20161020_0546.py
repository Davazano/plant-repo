# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20161020_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantimage',
            old_name='image',
            new_name='image_file',
        ),
        migrations.AddField(
            model_name='plantimage',
            name='image_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='image_description',
            field=models.TextField(blank=True),
        ),
    ]
