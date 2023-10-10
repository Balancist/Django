from django.contrib import admin
from .models import Topic, Sureh, Article, Comment

#actions
admin.actions.delete_selected.short_description = 'حذف'

def publish(modeladmin, request, queryset):
	queryset.update(status='P')
publish.short_description = 'انتشار'

def draft(modeladmin, request, queryset):
	queryset.update(status='D')
draft.short_description = 'پیش نویس'




#admins
class SurehAdmin(admin.ModelAdmin):
	list_display = ('name', 'number')
	search_fields = ('name', 'slug', 'number')


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('sureh', 'ayeh', 'topic_to_str')
	list_filter = ('update', 'status')
	search_fields = ('sureh', 'ayeh', 'topic_to_str', 'text')
	ordering = ['sureh', 'ayeh']
	actions = [publish, draft]


#registers
admin.site.register(Sureh, SurehAdmin)
admin.site.register(Topic)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)