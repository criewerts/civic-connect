# Generated by Django 3.1.1 on 2020-10-18 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civicconnect', '0004_auto_20201018_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='template',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]