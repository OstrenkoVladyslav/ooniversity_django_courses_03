from django.contrib import admin
from courses.models import Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display =  ['name', 'short_description']

class LessonInline(admin.StackedInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline,]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
# Register your models here.
