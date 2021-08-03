# Generated by Django 2.2.24 on 2021-08-02 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20210802_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myplaylist',
            name='mp_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='music_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='user_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
