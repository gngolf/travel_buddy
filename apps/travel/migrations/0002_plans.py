# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('plan', models.CharField(max_length=255)),
                ('start', models.CharField(max_length=100)),
                ('end', models.CharField(max_length=100)),
                ('user_id', models.ManyToManyField(to='travel.Users')),
            ],
        ),
    ]
