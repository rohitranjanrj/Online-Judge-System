# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-08 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20180908_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='error_file',
            field=models.FileField(default='submission/error/fb6694dd-0723-4fdc-955f-cf555b6f44be.txt', upload_to=''),
        ),
        migrations.AlterField(
            model_name='status',
            name='op_file',
            field=models.FileField(default='submission/output/2463ec51-dc36-4cd9-ab85-7c8cb99f34c6.txt', upload_to=''),
        ),
    ]
