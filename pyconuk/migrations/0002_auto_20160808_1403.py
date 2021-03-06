# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyconuk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='session',
            name='speaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyconuk.Speaker'),
        ),
    ]
