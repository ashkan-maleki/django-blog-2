# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160101_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 1, 14, 12, 40, 256000, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
