from django.urls import path
from . import views

app_name = 'Quran'
urlpatterns = [
	path('', views.Index.as_view(), name='index'),
	path('<slug:slug>/', views.SurehDetail.as_view(), name='sureh'),
	path('<slug:slug>/<int:ayeh>/article/', views.ArticleDetail.as_view(), name='article'),
	path('<slug:slug>/<int:ayeh>/article/comment/add/', views.AddComment.as_view(), name='add_comment')
]