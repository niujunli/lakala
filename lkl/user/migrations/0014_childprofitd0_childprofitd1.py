# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-05 19:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0013_auto_20180304_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildProfitD0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_id', models.CharField(max_length=64, unique=True, verbose_name='\u6d41\u6c34\u53f7')),
                ('fenrun_point', models.CharField(max_length=50, verbose_name='\u63d0\u70b9')),
                ('fenrun_rmb', models.CharField(max_length=50, verbose_name='\u79d2\u5230')),
                ('fenrun_father_point', models.CharField(max_length=50, verbose_name='\u5bfc\u5e08\u63d0\u70b9')),
                ('fenrun_father_rmb', models.CharField(max_length=50, verbose_name='\u5bfc\u5e08\u79d2\u5230')),
                ('rmb', models.IntegerField(verbose_name='\u5229\u6da6\u91d1\u989d(\u5206)')),
                ('merchant_code', models.CharField(max_length=64, verbose_name='\u5546\u6237\u53f7')),
                ('draw_date', models.CharField(max_length=64, verbose_name='\u63d0\u6b3e\u65e5\u671f')),
                ('draw_rmb', models.CharField(max_length=64, verbose_name='\u63d0\u6b3e\u91d1\u989d')),
                ('fee_rmb', models.CharField(max_length=64, verbose_name='\u63d0\u6b3e\u624b\u7eed\u8d39')),
                ('real_rmb', models.CharField(max_length=64, verbose_name='\u5b9e\u9645\u6263\u6b3e')),
                ('trans_type', models.CharField(max_length=64, verbose_name='\u4ea4\u6613\u7c7b\u578b')),
                ('trans_status', models.CharField(max_length=64, verbose_name='\u4ea4\u6613\u72b6\u6001')),
                ('status', models.CharField(choices=[(b'UP', '\u672a\u652f\u4ed8'), (b'PD', '\u5df2\u652f\u4ed8'), (b'SU', '\u6210\u529f')], default=b'UP', max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='\u5206\u7ea2\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'ordering': ['-pay_time'],
                'db_table': 'user_profit_child_d0',
                'verbose_name': '\u7528\u6237D0\u83b7\u5229\u8868',
                'verbose_name_plural': '\u7528\u6237D0\u83b7\u5229\u8868',
            },
        ),
        migrations.CreateModel(
            name='ChildProfitD1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_id', models.CharField(max_length=64, unique=True, verbose_name='\u6d41\u6c34\u53f7')),
                ('fenrun_point', models.CharField(max_length=50, verbose_name='\u63d0\u70b9')),
                ('fenrun_rmb', models.CharField(max_length=50, verbose_name='\u79d2\u5230')),
                ('fenrun_father_point', models.CharField(max_length=50, verbose_name='\u5bfc\u5e08\u63d0\u70b9')),
                ('fenrun_father_rmb', models.CharField(max_length=50, verbose_name='\u5bfc\u5e08\u79d2\u5230')),
                ('rmb', models.IntegerField(verbose_name='\u5229\u6da6\u91d1\u989d(\u5206)')),
                ('merchant_code', models.CharField(max_length=64, verbose_name='\u5546\u6237\u53f7')),
                ('draw_date', models.CharField(max_length=64, verbose_name='\u63d0\u6b3e\u65e5\u671f')),
                ('draw_rmb', models.CharField(max_length=64, verbose_name='\u63d0\u6b3e\u91d1\u989d')),
                ('fee_rmb', models.CharField(max_length=64, verbose_name='\u5546\u6237\u624b\u7eed\u8d39')),
                ('card_type', models.CharField(max_length=64, verbose_name='\u5361\u7c7b\u578b')),
                ('pay_date', models.CharField(max_length=64, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('terminal', models.CharField(max_length=64, verbose_name='PSAM\u5361\u53f7')),
                ('status', models.CharField(choices=[(b'UP', '\u672a\u652f\u4ed8'), (b'PD', '\u5df2\u652f\u4ed8'), (b'SU', '\u6210\u529f')], default=b'UP', max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='\u5206\u7ea2\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'ordering': ['-pay_time'],
                'db_table': 'user_profit_child_d1',
                'verbose_name': '\u7528\u6237D1\u83b7\u5229\u8868',
                'verbose_name_plural': '\u7528\u6237D1\u83b7\u5229\u8868',
            },
        ),
    ]