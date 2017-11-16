from core.models import Dated, Titled, Authored


class Post(Dated, Titled, Authored):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пост {self.title}'


class Comment(Dated, Titled, Authored):
    class Meta:
        verbose_name = 'Комменатрий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий {self.title}'
