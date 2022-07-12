# Generated by Django 4.0.5 on 2022-06-30 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_user_car_remove_user_history_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='carParking',
        ),
        migrations.AddField(
            model_name='carparking',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.car'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.brand'),
        ),
    ]