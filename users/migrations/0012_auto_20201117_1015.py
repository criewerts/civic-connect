# Generated by Django 3.1.1 on 2020-11-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20201117_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='state',
        ),
        migrations.AddField(
            model_name='customuser',
            name='state_cd',
            field=models.CharField(blank=True, max_length=2, verbose_name='State'),
        ),
    ]
