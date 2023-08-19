from django.urls import path

from study.apps import CourseConfig, LessonConfig
from rest_framework.routers import DefaultRouter

from study.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentsListAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),

                  # path('subscriptions/', SubscriptionView.as_view(), name='subscriptions'),

                  path('<int:pk>/subscriptions/', SubscriptionCreateAPIView.as_view(), name='subscriptions-create'),
                  path('subscriptions/delete/<int:pk>', SubscriptionDestroyAPIView.as_view(),
                       name='subscriptions-delete'),
              ] + router.urls
