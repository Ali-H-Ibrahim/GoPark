# Generated by Django 4.0.5 on 2022-07-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_reservation_reserved_period'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['start_date']},
        ),
        migrations.AlterField(
            model_name='car',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carparking',
            name='cost',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='history',
            name='total_payments',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='cost',
            field=models.IntegerField(max_length=10),
        ),
    ]
