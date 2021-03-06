# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-10 19:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0017_slkltoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='WXUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=128, unique=True, verbose_name='openid')),
                ('nickname', models.CharField(blank=True, max_length=64, verbose_name='\u6635\u79f0')),
                ('sex', models.CharField(blank=True, max_length=10, verbose_name='\u6027\u522b')),
                ('province', models.CharField(blank=True, max_length=64, verbose_name='\u7701\u4efd')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='\u57ce\u5e02')),
                ('country', models.CharField(blank=True, max_length=64, verbose_name='\u56fd\u5bb6')),
                ('headimgurl', models.CharField(blank=True, max_length=512, verbose_name='\u5934\u50cf')),
                ('unionid', models.CharField(blank=True, max_length=128, verbose_name='unionid')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'wx_user',
                'verbose_name': '\u5fae\u4fe1\u7528\u6237',
                'verbose_name_plural': '\u5fae\u4fe1\u7528\u6237',
            },
        ),
    ]
