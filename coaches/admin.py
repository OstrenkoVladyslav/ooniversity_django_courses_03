from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'gender', 'skype', 'description')
	search_fields = ('user__first_name', 'user__last_name', 'gender', 'skype', 'description')
	list_filter = (
        ('user__is_staff', admin.BooleanFieldListFilter),
    )

	def first_name(self, objct): return objct.user.first_name
	def last_name(self, objct): return objct.user.last_name

admin.site.register(Coach, CoachAdmin)
