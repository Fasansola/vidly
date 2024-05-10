from django.contrib import admin
from .models import Movie, Genre, Renter
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'daily_rate', 'number_in_stock', 'genre')
    exclude = ('date_created', )
    prepopulated_fields = {"slug": ('title', )}
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class RenterAdmin(admin.ModelAdmin):
    list_display = ('name', )
    filter_horizontal = ('movie', )

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Renter, RenterAdmin)