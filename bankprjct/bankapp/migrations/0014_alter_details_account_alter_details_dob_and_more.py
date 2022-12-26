# Generated by Django 4.1 on 2022-12-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0013_rename_image_category_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='account',
            field=models.CharField(choices=[('S', 'savings'), ('C', 'current')], max_length=30),
        ),
        migrations.AlterField(
            model_name='details',
            name='dob',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='details',
            name='phone',
            field=models.IntegerField(max_length=30),
        ),
    ]