from django.contrib import admin
from .models import Movie

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'year', 'description')
    list_display = ('name', 'year', 'description', 'released')
    list_filter = ('year', 'released')
    search_fields = ('name', 'description')
