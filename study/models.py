from django.db import models
from users.models import NULLABLE, User


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


class Course(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    image = models.ImageField(upload_to='media/catalog/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')
    """счетчик уроков"""
    lesson_count = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='количество уроков', default=None)

    def __str__(self):
        return f'{self.name} ({self.description}) ({self.lesson_count})'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


    """ Модель платежи"""
class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты')

    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='оплаченный урок')

    payment_sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=100, verbose_name='способ оплаты')
