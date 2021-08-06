# Generated by Django 2.2.5 on 2021-08-03 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0006_auto_20210803_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myplaylist',
            old_name='p_like',
            new_name='mp_like',
        ),
        migrations.RenameField(
            model_name='myplaylist',
            old_name='myplaylist_name',
            new_name='mp_title',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlistcomment',
            name='user_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]