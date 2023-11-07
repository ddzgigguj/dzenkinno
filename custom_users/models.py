from django.db import models
from django.contrib.auth.models import User


MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'Мужчина'),
    (FEMALE, 'Женщина')
)

class CustomUser(User):
    date_birth = models.DateField(verbose_name='Введите дату рождения')
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Укажите ваш пол он ламинат?')
    phone_number = models.CharField(max_length=13, default='левая', verbose_name='Введите номер правой ноги')
    address = models.CharField(max_length=200, verbose_name='Укажите адрес проживания где вы проживаете', null=True)
    education = models.CharField(max_length=500, verbose_name='Образование зачем надо', blank=True, null=True)
    work_experience = models.CharField(max_length=500, verbose_name='Опыт работы сващиком', blank=True, null=True)
    image = models.ImageField(verbose_name='Загрузите фото профиля')

class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите имя', null=True)
    image = models.ImageField(verbose_name='Загрузите фото')

    def __str__(self):
        return self.name