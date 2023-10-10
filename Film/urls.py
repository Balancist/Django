from django.urls import path
from . import views

app_name = 'Film'
urlpatterns = [
	path('', views.index, name='index'),
	path('film/', views.film, name='film'),
	path('film/<int:page>/', views.film, name='film'),
	path('serie/', views.serie, name='serie'),
	path('serie/<int:page>/', views.serie, name='serie'),
	path('company/', views.company, name='company'),
	path('stream/', views.stream, name='stream'),
	path('genre/', views.genre, name='genre'),
	path('collection/', views.collection, name='collection'),
	path('company/<slug:slug>/', views.company_detail, name='company_detail'),
	path('stream/<slug:slug>/', views.stream_detail, name='stream_detail'),
	path('genre/<slug:slug>/', views.genre_detail, name='genre_detail'),
	path('collection/<slug:slug>/', views.collection_detail, name='collection_detail'),
	path('film/<slug:slug>/', views.film_detail, name='film_detail'),
	path('serie/<slug:slug>/', views.serie_detail, name='serie_detail'),
	path('serie/<slug:slug>/<slug:eslug>/', views.episode, name='episode')
]