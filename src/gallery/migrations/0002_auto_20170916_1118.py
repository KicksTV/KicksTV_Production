# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-16 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image',
            field=models.FileField(upload_to='gallery_img'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_image',
            field=models.FileField(upload_to='Image_img'),
        ),
    ]
