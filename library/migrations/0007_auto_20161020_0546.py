# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20161020_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantimage',
            name='image_file',
            field=models.FileField(upload_to=''),
        ),
    ]
