from core.models import Dated, Titled, Authored
from django.db import models


class Post(Dated, Titled, Authored):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'Пост {self.title}'


class Comment(Dated, Titled, Authored):
    class Meta:
        verbose_name = 'Комменатрий'
        verbose_name_plural = 'Комментарии'

    post = models.ForeignKey(Post, verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'Комментарий {self.title}'
