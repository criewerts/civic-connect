# Generated by Django 3.1.1 on 2020-10-23 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civicconnect', '0009_auto_20201023_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 2, 14, 58, 538017)),
        ),
    ]
