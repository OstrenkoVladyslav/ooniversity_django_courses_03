from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
  model = Lesson
  fields = [ 'subject', 'description' , 'order' ]

class CourseAdmin(admin.ModelAdmin):
  list_display = ['name', 'short_description']
  search_fields = ['name']
  fields = [ 'name', 'short_description', 'description' ]
  inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)