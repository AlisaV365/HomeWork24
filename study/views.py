from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from study.paginators import StudyPaginator
from study.permissions import IsModerator, IsOwner

from users.models import User
from study.models import Course, Lesson, Payments, Subscription
from study.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer
from rest_framework.views import APIView

# from rest_framework_simplejwt.views import TokenObtainPairView


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsAdminUser]
    pagination_class = StudyPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator]
    # pagination_class = StudyPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    # permission_classes = [IsAdminUser]


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    # filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ['paid_course', 'paid_lesson', 'payment_method']  # Набор полей для фильтрации
    ordering_fields = ('payment_date',)  # Сортировка по дате оплаты



    """Создание и удаление подписки"""

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsModerator | IsOwner]

    class SubscriptionView(APIView):
        def post(self, request, format=None):
            user_id = request.data.get('user_id')
            course_id = request.data.get('course_id')

            try:
                user = User.objects.get(id=user_id)
                course = Course.objects.get(id=course_id)

                subscription = Subscription(user=user, course=course)
                subscription.save()

                return Response("Подписка создана", status=status.HTTP_201_CREATED)
            except (User.DoesNotExist, Course.DoesNotExist):
                return Response("Пользователь или курс не существует", status=status.HTTP_404_NOT_FOUND)




class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, format=None):
        user_id = request.data.get('user_id')
        course_id = request.data.get('course_id')

        try:
            subscription = Subscription.objects.get(user_id=user_id, course_id=course_id)
            subscription.delete()

            return Response("Подписка удалена", status=status.HTTP_204_NO_CONTENT)
        except Subscription.DoesNotExist:
            return Response("Подписка не существует", status=status.HTTP_404_NOT_FOUND)

