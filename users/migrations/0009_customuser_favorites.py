# Generated by Django 3.1.1 on 2020-11-09 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civicconnect', '0024_auto_20201108_2206'),
        ('users', '0008_delete_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(blank=True, to='civicconnect.Template'),
        ),
    ]