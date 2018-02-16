# Generated by Django 2.0.2 on 2018-02-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='발매일')),
                ('genre', models.CharField(max_length=30, verbose_name='장르')),
                ('FLAC', models.CharField(max_length=30, null=True, verbose_name='FLAC')),
            ],
        ),
    ]