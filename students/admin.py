from django.contrib import admin
from students.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    search_fields = ['surname', 'email']
    list_filter = ['courses']

admin.site.register(Student, StudentAdmin)


