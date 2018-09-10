# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-03 07:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import submission.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('judge', '0004_auto_20180824_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=' ', max_length=100)),
                ('language', models.IntegerField(blank=True, null=True)),
                ('submissiontime', models.DateTimeField(auto_now=True)),
                ('time', models.DecimalField(decimal_places=2, max_digits=5)),
                ('result', models.CharField(default=' ', max_length=10)),
                ('source_code', models.FileField(blank=True, null=True, upload_to=submission.models.random_source_code_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'], message="Please upload '.py' files only.")])),
                ('op_file', models.FileField(upload_to='submission/output/')),
                ('error_file', models.FileField(upload_to='submission/error/')),
                ('quesid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.question')),
            ],
        ),
    ]
