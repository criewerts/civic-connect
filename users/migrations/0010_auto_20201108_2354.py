# Generated by Django 3.1.1 on 2020-11-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civicconnect', '0025_auto_20201108_2354'),
        ('users', '0009_customuser_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorites_topic',
            field=models.ManyToManyField(to='civicconnect.Topic'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(to='civicconnect.Template'),
        ),
    ]
