# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(default=datetime.datetime(2015, 12, 22, 17, 48, 51, 82000, tzinfo=utc), verbose_name=b'date published')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
