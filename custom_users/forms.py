from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'паркет'),
    (FEMALE, 'ламинат')
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_birth = forms.DateField(required=True, label='Введите дату рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True, label='Укажите ваш пол он ламинат?')
    phone_number = forms.CharField(required=True, max_length=13, initial='левая', label='Введите номер правой ноги')
    address = forms.CharField(max_length=200, required=True, label='Укажите адрес проживания где вы проживаете')
    education = forms.CharField(max_length=500, required=True, label='Образование зачем надо')
    work_experience = forms.CharField(max_length=500, required=True, label='Опыт работы сващиком')
    image = forms.ImageField(required=True, label='Загрузите фото профиля')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'date_birth',
            'gender',
            'phone_number',
            'address',
            'education',
            'work_experience',
            'image',
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user