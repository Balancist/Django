from django.contrib import admin
from .models import Company, Stream, Genre, Collection, Film, Serie, Episode

#admins
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name', 'logo_tag', 'mother', 'year')
	search_fields = ('name', 'mother', 'year')
	ordering = ['year']


class StreamAdmin(admin.ModelAdmin):
	list_display = ('name', 'logo_tag', 'year')
	search_fields = ('name', 'year')
	ordering = ['year']


class GenreAdmin(admin.ModelAdmin):
	search_fields = ('name', 'slug')
	ordering = ['name']


class CollectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'chapter')
	search_fields = ('name', 'slug')
	ordering = ['name']


class FilmAdmin(admin.ModelAdmin):
	list_display = ('title', 'poster_tag', 'genre_to_str', 'year', 'company_to_str')
	list_filter = ('year', 'genre', 'company', 'kind')
	search_fields = ('title', 'slug', 'genre_to_str', 'year', 'company_to_str')
	ordering = ['-year', 'title']


class SerieAdmin(admin.ModelAdmin):
	list_display = ('title', 'poster_tag', 'season', 'first', 'last', 'status', 'genre_to_str', 'company_to_str', 'stream')
	list_filter = ('kind', 'status', 'genre', 'company', 'stream')
	search_fields = ('title', 'slug', 'genre_to_str', 'company_to_str', 'stream')
	ordering = ['title']


class EpisodeAdmin(admin.ModelAdmin):
	list_display = ('serie', 'slug', 'size')
	search_fields = ('serie', 'slug')
	ordering = ['serie', 'slug']



#registers
admin.site.register(Company, CompanyAdmin)
admin.site.register(Stream, StreamAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Episode, EpisodeAdmin)