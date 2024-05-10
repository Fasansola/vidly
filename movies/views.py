from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, Renter
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "movies/index.html", {
        "movies": Movie.objects.all()
    })
    
def details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, "movies/detail.html", {
        "movie": movie,
        "renters": movie.renter.all(),
        "non_renters": Renter.objects.exclude(movie=movie).all()
    })
    
def rent(request, slug):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, slug=slug)
        renter = Renter.objects.get(pk=int(request.POST["renter"]))
        renter.movie.add(movie)
        
    return HttpResponseRedirect(reverse('movies:detail', args=(slug, )))