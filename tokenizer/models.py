from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model
from django.utils import timezone


class Url(models.Model):
    url = models.URLField(
        verbose_name='Ссылка',
        max_length=2048
    )
    token = models.CharField(
        max_length=16,
        help_text='Сокращенная ссылка',
        unique=True
    )
    creation_time = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    redirect_count = models.IntegerField(
        verbose_name='Количество переходов по ссылке',
        default=0
    )
