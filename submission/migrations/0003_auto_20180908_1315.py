# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-08 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20180908_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='op_file',
            field=models.FileField(default='submission/output/dcf6a349-d038-4890-8766-dec4dfb85577.txt', upload_to=''),
        ),
    ]
