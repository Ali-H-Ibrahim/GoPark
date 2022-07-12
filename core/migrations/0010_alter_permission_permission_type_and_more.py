# Generated by Django 4.0.5 on 2022-07-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_carparking_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='permission_type',
            field=models.CharField(choices=[('Garage Manager', 'Garage Manager'), ('Cashier', 'Cashier'), ('Customer', 'Customer')], max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_type',
            field=models.CharField(choices=[('One Time', 'one time'), ('Daily', 'Daily'), ('Weekly', 'Weekly')], max_length=100),
        ),
    ]