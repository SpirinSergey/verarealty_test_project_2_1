# Generated by Django 4.0 on 2021-12-10 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_listing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='FLOOR_PLAN',
        ),
    ]
