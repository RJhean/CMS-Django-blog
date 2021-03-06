# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Search')),
            ],
            options={
                'verbose_name_plural': 'Ключевые слова',
                'db_table': 'keywords',
                'verbose_name': 'Ключевое слово',
            },
        ),
    ]
