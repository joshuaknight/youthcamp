# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-24 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0005_article_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_article',
            name='article_comment_key',
        ),
    ]