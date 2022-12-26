# Generated by Django 4.1 on 2022-12-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0008_alter_details_gender_alter_details_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'ot,her')], max_length=30),
        ),
        migrations.AlterField(
            model_name='details',
            name='material',
            field=models.CharField(choices=[('debitcard', 'debitcard'), ('creditacrd', 'creditcard'), ('prepaidcard', 'prepaidcard'), ('cheque', 'cheque')], default=2, max_length=150),
            preserve_default=False,
        ),
    ]