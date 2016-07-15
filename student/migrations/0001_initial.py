# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, validators=[student.models.validate_name])),
                ('last_name', models.CharField(max_length=20, validators=[student.models.validate_name])),
                ('father_name', models.CharField(max_length=20, validators=[student.models.validate_name])),
                ('mother_name', models.CharField(max_length=20, validators=[student.models.validate_name])),
                ('annual_income', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('faith_home', models.CharField(max_length=20)),
            ],
        ),
    ]
