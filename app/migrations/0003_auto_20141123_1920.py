# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141118_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='Average_amount_for_month',
            new_name='average_amount_for_month',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='At_day_time',
            new_name='at_day_time',
        ),
        migrations.RenameField(
            model_name='time',
            old_name='DateTime',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Bill',
            new_name='bill',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
    ]
