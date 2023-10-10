from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Company, Stream, Genre, Collection, Film, Serie, Episode

def index(request):
	return render(request, 'film/index.html', {'films': Film.objects.all(),'series': Serie.objects.all()})

def film(request, page=1):
	all_films = Film.objects.all()
	paginator = Paginator(all_films, 10)
	films = paginator.get_page(page)
	return render(request, 'film/film.html', {'films': films})

def serie(request, page=1):
	all_series = Serie.objects.all()
	paginator = Paginator(all_series, 10)
	series = paginator.get_page(page)
	return render(request, 'film/serie.html', {'series': series})

def company(request):
	return render(request, 'film/company.html', {'companies': Company.objects.all()})

def stream(request):
	return render(request, 'film/stream.html', {'streams': Stream.objects.all()})

def genre(request):
	return render(request, 'film/genre.html', {'genres': Genre.objects.all()})

def collection(request):
	return render(request, 'film/collection.html', {'collections': Collection.objects.all()})

def company_detail(request, slug):
	return render(request, 'film/company_detail.html', {'company': get_object_or_404(Company, slug=slug)})

def stream_detail(request, slug):
	return render(request, 'film/stream_detail.html', {'stream': get_object_or_404(Stream, slug=slug)})

def genre_detail(request, slug):
	return render(request, 'film/genre_detail.html', {'genre': get_object_or_404(Genre, slug=slug)})

def collection_detail(request, slug):
	return render(request, 'film/collection_detail.html', {'collection': get_object_or_404(Collection, slug=slug)})

def film_detail(request, slug):
	return render(request, 'film/film_detail.html', {'film': get_object_or_404(Film, slug=slug)})

def serie_detail(request, slug):
	return render(request, 'film/serie_detail.html', {'serie': get_object_or_404(Serie, slug=slug)})

def episode(request, slug, eslug):
	return render(request, 'film/episode.html', {'episode': get_object_or_404(Episode, serie__slug=slug, slug=eslug)})