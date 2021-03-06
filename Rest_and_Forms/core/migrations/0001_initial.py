# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_img', models.FileField(blank=True, null=True, upload_to=utils.get_file_path)),
                ('about', models.TextField()),
                ('terms_of_service', models.TextField()),
                ('privacy_policy', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
