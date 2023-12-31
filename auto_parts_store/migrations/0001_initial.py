# Generated by Django 4.2.6 on 2023-10-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название товара')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Загрузите фото')),
                ('description', models.TextField(verbose_name='Укажите описание товара')),
                ('car_brand', models.CharField(choices=[('Mitsubishi', 'Mitsubishi'), ('Jeep', 'Jeep'), ('Land Rover', 'Land Rover'), ('Isuzu', 'Isuzu'), ('Nissan', 'Nissan'), ('Toyota', 'Toyota'), ('Ford', 'Ford')], max_length=100, verbose_name='Выберите марку автомобиля')),
                ('year_of_release', models.CharField(choices=[('1980-1984', '1980-1984'), ('1985-1989', '1985-1989'), ('1990-1994', '1990-1994'), ('1995-1999', '1995-1999'), ('2000-2004', '2000-2004'), ('2005-2009', '2005-2009'), ('2010-2014', '2010-2014'), ('2015-2019', '2015-2019'), ('2020-2023', '2020-2023')], max_length=100, verbose_name='Выберите год выпуска')),
                ('review_of_the_car', models.URLField(blank=True, verbose_name='Укажите видео обзор автомобиля')),
                ('review_of_auto_parts', models.URLField(blank=True, verbose_name='Укажите видео обзор автозапчасти')),
                ('cost', models.PositiveIntegerField(verbose_name='Укажите цену')),
                ('tel_number', models.IntegerField(max_length=10, verbose_name='Укажите номер телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
