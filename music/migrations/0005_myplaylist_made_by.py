# Generated by Django 2.2.5 on 2021-08-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20210802_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='myplaylist',
            name='made_by',
            field=models.IntegerField(default=0),
        ),
    ]