# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('away_score', models.PositiveIntegerField(null=True, blank=True)),
                ('home_score', models.PositiveIntegerField(null=True, blank=True)),
                ('week', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(22)])),
                ('spread', models.FloatField(default=0)),
                ('status', models.CharField(default=b'OTHER_UNAVAILABLE', max_length=30, choices=[(b'NOT_YET_STARTED', b'Not yet started'), (b'IN_PROGRESS', b'In progress'), (b'COMPLETE', b'Complete'), (b'OTHER_AVAILABLE', b'Other - available'), (b'OTHER_UNAVAILABLE', b'Other - unavailable')])),
                ('date_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pick', models.CharField(max_length=4, choices=[(b'H', b'home'), (b'A', b'away')])),
                ('game', models.ForeignKey(related_name=b'picks', to='pickem_app.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pickset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(22)])),
                ('attempts', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(16)])),
                ('correct', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(16)])),
                ('gametype', models.CharField(default=b'ATS', max_length=19, choices=[(b'SU', b'straight-up'), (b'ATS', b'against the spread')])),
                ('user', models.ForeignKey(related_name=b'picksets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbreviation', models.CharField(unique=True, max_length=5)),
                ('location', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pick',
            name='pickset',
            field=models.ForeignKey(related_name=b'picks', to='pickem_app.Pickset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(related_name=b'away_games', to='pickem_app.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(related_name=b'home_games', to='pickem_app.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='spread_winner',
            field=models.ForeignKey(related_name=b'games_won_ats', blank=True, to='pickem_app.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(related_name=b'games_won_su', blank=True, to='pickem_app.Team', null=True),
            preserve_default=True,
        ),
    ]
