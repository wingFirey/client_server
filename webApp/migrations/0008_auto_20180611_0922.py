# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_auto_20180611_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='other_details',
            field=models.CharField(help_text='Other Details', max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_ID',
            field=models.CharField(help_text='Patient ID', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_age',
            field=models.CharField(help_text=' Age', max_length=5),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_issue',
            field=models.CharField(help_text='Issue', max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(help_text='Name', max_length=30),
        ),
    ]