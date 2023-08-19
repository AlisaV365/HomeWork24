import json

from django.urls import reverse
from rest_framework import status
from rest_framework.templatetags.rest_framework import data
from rest_framework.test import APITestCase

from study.models import Course, Lesson, Subscription
from users.models import User


class StudyTestCase(APITestCase):

    def setUp(self) -> None:
        self.lesson = Lesson.objects.create(
            name='Test',
            description='test'
        )

        self.course = Course.objects.create(
            name='Test',
            description='test'
        )
        self.user = User.objects.create(
            email='avt758018@yandex.ru'
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

    def test_create_course(self):
        """Тестирование создания курса"""
        data = {
            'name': 'Test',
            'description': 'test',
        }

        response = self.client.post(
            '/course/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""
        response = self.client.get(
            reverse('study:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()[0],
            {
                "id": self.lesson.id,
                "urlvideo": self.lesson.urlvideo,
                "name": self.lesson.name,
                "description": self.lesson.description,
                "image": self.lesson.image,
                "course_id": self.lesson.course_id_id,
                "owner_id": self.lesson.owner_id
            }
        )

    def test_create_lesson(self):
        """Тестирование cоздания уроков"""

        data = {
            'name': 'Test3',
            'description': 'test3',
            'urlvideo': 'https://youtube.com'
        }

        response = self.client.post(
            reverse('study:lesson_create'),
            data=data
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_create_lesson_validation_error(self):
        """Тестирование валидации уроков"""

        data = {
            'name': 'Test2.1',
            'description': 'test2.1',
            'urlvideo': 'https://youtubchik.com'
        }

        response = self.client.post(
            reverse('study:lesson_create'),
            data=data
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_retrieve_lesson(self):
        """Тестирование вывода урока"""
        data = {
            'name': 'Test3',
            'description': 'test3',
            'urlvideo': 'https://youtube.com'
        }

        response = self.client.get(
            reverse('study:lesson_get', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """Тестирование обновления уроков"""
        data = {
            'name': 'Tests',
            'description': 'testNewsss',
            'urlvideo': 'https://youtube.com'
        }

        response = self.client.put(
            reverse('study:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.name,
            'Tests'
        )

        self.assertEqual(
            self.lesson.description,
            'testNewsss'
        )

    def test_delete_lesson(self):
        """Тестирование удаления уроков"""
        url = reverse(
            'study:lesson_delete', args=[self.lesson.pk]
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.filter(pk=self.lesson.pk).exists()
        )

    def test_subscription_creation(self):
        """Тестирование создания подписки"""

        subscription_exists = Subscription.objects.filter(user=self.user, course=self.course).exists()
        if not subscription_exists:
            subscription = Subscription.objects.create(user=self.user, course=self.course)

            self.assertEqual(
                subscription.user, self.user
            )
            self.assertEqual(
                subscription.course, self.course
            )
            self.assertTrue(
                subscription.is_active
            )
            self.assertFalse(
                subscription.is_paid
            )
        else:
            self.fail("Подписка с таким пользователем и курсом уже существует")


def test_cancel_subscription(self):
        """Тестирование отмены подписки"""
        self.subscription.is_active = False

        self.subscription.save()
        cancelled_subscription = Subscription.objects.get(
            user=self.user,
            course=self.course
        )

        self.assertFalse(
            cancelled_subscription.is_active
        )


