# Generated by Django 4.2.6 on 2023-11-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Укажите адрес проживания'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='education',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='work_experience',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Опыт работы'),
        ),
    ]
