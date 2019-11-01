# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-01 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher')),
            ],
        ),
    ]
