from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Home.views import send_request, verify
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('request/', send_request, name='request'),
    path('verify/', verify, name='verify'),
    path('film/', include('Film.urls')),
    path('quran/', include('Quran.urls')),
    path('justice/', include('Justice.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)