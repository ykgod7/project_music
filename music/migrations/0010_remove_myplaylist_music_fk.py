# Generated by Django 2.2.5 on 2021-08-03 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20210803_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myplaylist',
            name='music_fk',
        ),
    ]
