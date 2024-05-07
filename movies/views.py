from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    return render(request, "movies/index.html", {
        "movies": Movie.objects.all()
    })
    
def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/detail.html", {
        "movie": movie
    })