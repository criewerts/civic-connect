# Generated by Django 3.1.1 on 2020-10-24 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civicconnect', '0019_auto_20201024_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 24, 15, 8, 37, 189676)),
        ),
    ]