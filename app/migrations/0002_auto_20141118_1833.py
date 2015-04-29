# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='BillID',
            new_name='Bill',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TimeID',
            new_name='Time',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='UserID',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='BillID',
        ),
        migrations.RemoveField(
            model_name='time',
            name='TimeID',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='TransactionID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='UserID',
        ),
    ]
