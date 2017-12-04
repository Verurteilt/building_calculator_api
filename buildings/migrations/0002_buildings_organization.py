# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildings',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organizations'),
            preserve_default=False,
        ),
    ]
