# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('array', json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object')),
                ('ndim', models.IntegerField(default=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieRated',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('movie', models.CharField(max_length=100)),
                ('movieindx', models.IntegerField(default=-1)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('array', json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object')),
                ('arrayratedmoviesindxs', json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object')),
                ('name', models.CharField(max_length=1000)),
                ('lastrecs', json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object')),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movierated',
            name='user',
            field=models.ForeignKey(related_name='ratedmovies', to='books_app.UserProfile'),
        ),
    ]
