# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20171130_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=225, unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('upc', models.CharField(max_length=255, null=True)),
                ('shipping', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('manufacturer', models.CharField(max_length=255, null=True)),
                ('model', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=products.models.upload_image_path)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
        ),
    ]
