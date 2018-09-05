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
    )
    creation_time = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now
    )
    redirect_count = models.IntegerField(
        verbose_name='Количество переходов по ссылке',
    )