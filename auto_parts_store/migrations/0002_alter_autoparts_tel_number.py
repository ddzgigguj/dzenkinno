# Generated by Django 4.2.6 on 2023-10-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parts_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoparts',
            name='tel_number',
            field=models.IntegerField(verbose_name='Укажите номер телефона'),
        ),
    ]
