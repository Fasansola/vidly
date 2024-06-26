from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name.capitalize()
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.title.capitalize()
    
class Renter(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, blank=True, related_name="renter")
    
    def __str__(self):
        return self.name
    