# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to=b'art', verbose_name='Image')),
                ('technique', models.TextField(blank=True, null=True, verbose_name='Technique')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
