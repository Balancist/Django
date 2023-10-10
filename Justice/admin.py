from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Crime, Culprit, Complaint

#admins
UserAdmin.fieldsets[1][1]['fields'] += ('phone_number',)
UserAdmin.fieldsets[2][1]['fields'] = ("is_active", "is_superuser", 'is_valid', "groups", "user_permissions")
UserAdmin.list_display += ('phone_number', 'is_valid')
UserAdmin.list_filter += ('is_valid',)
UserAdmin.search_fields += ('phone_number',)

class CrimeAdmin(admin.ModelAdmin):
	search_fields = ('name', 'slug', 'law')
	ordering = ['name']


class CulpritAdmin(admin.ModelAdmin):
	search_fields = ('first_name', 'last_name')


#registers
admin.site.register(User, UserAdmin)
admin.site.register(Crime, CrimeAdmin)
admin.site.register(Culprit)
admin.site.register(Complaint)