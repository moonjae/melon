# Generated by Django 2.0.2 on 2018-02-07 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20180207_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='song',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='song',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
