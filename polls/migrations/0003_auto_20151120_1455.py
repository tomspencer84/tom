# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151120_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=b'default', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=1, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 14, 55, 22, 252000, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=b'default', max_length=200),
        ),
    ]
