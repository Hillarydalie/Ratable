# Generated by Django 2.2.4 on 2019-11-18 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KPIs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='area',
        ),
    ]
