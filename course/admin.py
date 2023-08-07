from django.contrib import admin

from course.models import Course


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
