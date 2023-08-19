from rest_framework import serializers
from study.models import Course, Lesson, Payments, Subscription
from study.validators import validator_urlvideo


class LessonSerializer(serializers.ModelSerializer):
    urlvideo = serializers.URLField(validators=[validator_urlvideo])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    """ Счетчик уроков"""

    def get_lessons_count(self, instance):
        return instance.lesson.all().count()


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

        """ Сериалайзер подписки"""

class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ['user', 'course', 'subscribed_at', 'is_active', 'is_paid', 'is_subscribed']