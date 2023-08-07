from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    image = models.ImageField(upload_to='media/catalog/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

