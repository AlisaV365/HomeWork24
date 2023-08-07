from django.db import models

from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/catalog/', verbose_name='картинка', **NULLABLE)
    urlvideo = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
