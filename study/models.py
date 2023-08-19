from django.conf import settings
from django.db import models
from users.models import NULLABLE, User


class Course(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    image = models.ImageField(upload_to='media/catalog/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')
    owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', related_name='course_author',
                                 **NULLABLE)

    lesson_count_id = models.IntegerField(verbose_name='Кол-во уроков', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='media/catalog/', verbose_name='картинка', **NULLABLE)
    urlvideo = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='курс', related_name='lesson',
                                  **NULLABLE)
    owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', related_name='lesson_author',
                                 **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    """ Модель платежи"""


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты')

    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='payments')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='payments')

    payment_sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=100, verbose_name='способ оплаты')

    """ Модель подписки"""


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name='дата подписки')
    is_active = models.BooleanField(default=True, verbose_name='подписан')
    is_paid = models.BooleanField(default=False, verbose_name='оплачено')

    def __str__(self):
        return f'{self.user} подписан на курс {self.course}' if self.is_active else f'{self.user} отписался от курса {self.course}'

    class Meta:
        unique_together = ['user', 'course']
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
