# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-10 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160410_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./user_images/'),
        ),
    ]
