# Generated by Django 4.0.5 on 2022-06-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='model',
            field=models.CharField(max_length=200, null=True),
        ),
    ]