# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import webApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0010_patient_patient_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_file',
            field=models.ImageField(blank=True, null=True, upload_to=webApp.models.upload_location),
        ),
    ]