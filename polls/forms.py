from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.forms import TextInput
from .models import AbsUser


class RegisterUserForm(forms.ModelForm):
    last_name = forms.CharField(label='Фамилия',
                                error_messages={
                                    'required': 'Обязательное поле',
                                }, )
    first_name = forms.CharField(label='Имя',
                                 error_messages={
                                     'required': 'Обязательное поле',
                                 })
    username = forms.CharField(label='Логин',
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Данный логин занят'
                               })
    password = forms.CharField(label='Пароль',
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    password2 = forms.CharField(label='Пароль (повторно)',
                                error_messages={
                                    'required': 'Обязательное поле',
                                })
    photo = forms.ImageField(label='Фото')

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Пароли не совпадают', code='pass_error')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = AbsUser
        fields = ('last_name', 'first_name', 'username', 'password', 'password2', 'photo')
        enctype = "multipart/form-data"


