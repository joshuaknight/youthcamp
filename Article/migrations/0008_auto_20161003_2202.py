# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0007_author_detail_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_article',
            name='published_till_now',
        ),
        migrations.DeleteModel(
            name='Author_Detail',
        ),
    ]
