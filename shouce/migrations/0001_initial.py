# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shouce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u624b\u518c\u540d\u79f0')),
                ('url', models.URLField(max_length=300, verbose_name='\u94fe\u63a5')),
                ('desc', models.TextField(verbose_name='\u7b80\u4ecb')),
                ('ctime', models.DateTimeField(null=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.Language')),
            ],
            options={
                'verbose_name': '\u624b\u518c',
                'verbose_name_plural': '\u624b\u518c',
            },
        ),
    ]
