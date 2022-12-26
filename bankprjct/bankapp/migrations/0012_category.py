# Generated by Django 4.1 on 2022-12-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0011_alter_details_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
        ),
    ]
