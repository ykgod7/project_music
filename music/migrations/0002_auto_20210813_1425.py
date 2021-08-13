# Generated by Django 2.2.5 on 2021-08-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='m_videoCd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='music',
            field=models.ManyToManyField(blank=True, related_name='mlike_users', to='music.Music'),
        ),
    ]