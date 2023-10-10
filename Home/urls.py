from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
	path('', views.index, name='index'),
	path('search/', views.Search.as_view(), name='search'),
	path('search/<int:page>/', views.Search.as_view(), name='search')
]