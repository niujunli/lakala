# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-04 00:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0011_auto_20180224_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='FenRunOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(verbose_name='\u5206\u6da6\u70b9')),
                ('rmb', models.IntegerField(verbose_name='\u79d2\u5230\u70b9')),
                ('status', models.CharField(choices=[(b'WAIT', '\u7b49\u5f85\u5ba1\u6838'), (b'PASS', '\u5ba1\u6838\u901a\u8fc7'), (b'OK', '\u5b8c\u6210')], default=b'WAIT', max_length=10, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('pass_time', models.DateTimeField(blank=True, null=True, verbose_name='\u5ba1\u6838\u65f6\u95f4')),
                ('finish_time', models.DateTimeField(blank=True, null=True, verbose_name='\u5b8c\u7ed3\u65f6\u95f4')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fenrun_target', to=settings.AUTH_USER_MODEL, verbose_name='\u4e0b\u5bb6')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fenrun_asker', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'ordering': ['-pass_time'],
                'db_table': 'user_fenrun_order',
                'verbose_name': '\u5206\u6da6\u7533\u8bf7\u8868',
                'verbose_name_plural': '\u5206\u6da6\u7533\u8bf7\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='userrmb',
            options={'ordering': ['-rmb', '-child_rmb'], 'verbose_name': '\u7528\u6237\u91d1\u94b1\u8868', 'verbose_name_plural': '\u7528\u6237\u91d1\u94b1\u8868'},
        ),
        migrations.AlterField(
            model_name='userfenrun',
            name='point',
            field=models.CharField(choices=[(b'5.0', '5.0'), (b'5.5', '5.5'), (b'6.0', '6.0'), (b'6.5', '6.5'), (b'7.0', '7.0'), (b'7.5', '7.5'), (b'8.0', '8.0'), (b'8.5', '8.5'), (b'9.0', '9.0'), (b'9.5', '9.5'), (b'10.0', '10.0')], max_length=50, verbose_name='\u63d0\u70b9'),
        ),
    ]
