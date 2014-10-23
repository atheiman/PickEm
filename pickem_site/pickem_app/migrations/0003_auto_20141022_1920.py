# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pickem_app', '0002_auto_20141022_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickset',
            name='score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(16), django.core.validators.MinValueValidator(-16)]),
        ),
    ]
