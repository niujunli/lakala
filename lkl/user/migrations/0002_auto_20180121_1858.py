# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-21 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name': '用户地址', 'verbose_name_plural': '用户地址'},
        ),
        migrations.AlterModelOptions(
            name='userpos',
            options={'verbose_name': '用户POS机', 'verbose_name_plural': '用户POS机'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户属性', 'verbose_name_plural': '用户属性'},
        ),
        migrations.AlterModelOptions(
            name='usertrade',
            options={'verbose_name': '用户交易记录', 'verbose_name_plural': '用户交易记录'},
        ),
    ]
