# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-24 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0010_remove_new_article_object_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_comment',
            name='object_id',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]