from rest_framework import serializers
from study.models import Course, Lesson, Payments


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    """ вывод количества уроков """

    def get_lesson_count(self, course):
        return course.lesson_set.count()

    """ список уроков"""
    def get_lessons(self, instance):
        if instance.course.lesson_set.all():
            return instance.course.lesson_set.all().lessons
        return 0

    class Meta:
        model = Course
        fields = ['id', 'name', 'image', 'description', 'lesson_count', 'lessons']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
