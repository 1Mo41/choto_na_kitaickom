import datetime
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + ' ' + filename])


def validate_image_size(img):
    filesize = img.file.size
    megabyte_max = 2.0
    if filesize > megabyte_max * 1024 * 1024:
        raise ValidationError("Максимальный размер %sMB" % str(megabyte_max))


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class AbsUser(AbstractUser):
    first_name = models.CharField(max_length=60, verbose_name='Имя', blank=False)
    last_name = models.CharField(max_length=60, verbose_name='Фамилия', blank=False)
    username = models.CharField(max_length=60, verbose_name='Логин', unique=True, blank=False)
    password = models.CharField(max_length=60, verbose_name='Пароль', unique=True, blank=False)
    photo = models.ImageField(upload_to=get_name_file,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp']),
                                          validate_image_size],
                              blank=False)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name) + ' (' + str(self.username) + ')'
