# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-07 12:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xyf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='XYFPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn_code', models.CharField(max_length=64, unique=True, verbose_name='SN\u53f7')),
                ('terminal', models.CharField(blank=True, max_length=64, verbose_name='\u7ec8\u7aef\u53f7')),
                ('is_activate', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'db_table': 'xyf_pos',
                'verbose_name': '\u661f\u9a7f\u4ed8POS\u673a',
                'verbose_name_plural': '\u661f\u9a7f\u4ed8POS\u673a',
            },
        ),
        migrations.AlterModelOptions(
            name='syfterminal',
            options={'ordering': ['-bind_date'], 'verbose_name': '\u6fc0\u6d3b\u5546\u6237\u7ba1\u7406', 'verbose_name_plural': '\u6fc0\u6d3b\u5546\u6237\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='syftrade',
            options={'ordering': ['-trade_date'], 'verbose_name': '\u4ea4\u6613\u660e\u7ec6', 'verbose_name_plural': '\u4ea4\u6613\u660e\u7ec6'},
        ),
        migrations.AlterField(
            model_name='syftrade',
            name='consume_type',
            field=models.CharField(max_length=64, verbose_name='\u6d88\u8d39\u7c7b\u578b'),
        ),
    ]
