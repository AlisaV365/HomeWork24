from django.contrib import admin

from study.models import Course, Lesson, Payments, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'paid_course', 'paid_lesson', 'payment_sum', 'payment_method')


@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = ('user', 'course', 'subscribed_at', 'is_active', 'is_paid')
