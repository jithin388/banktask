# Generated by Django 4.1 on 2022-12-24 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_alter_details_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='gender',
        ),
    ]
