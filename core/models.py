from django.db import models
from django.conf import settings


class Dated(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


class Titled(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(verbose_name='Название', max_length=128)


class Authored(models.Model):
    class Meta:
        abstract = True

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор')
