from django.contrib import admin
from .models import Customer
from django.contrib import admin
from.models import movie
from.models import newmovie
from.models import series
from.models import newseries
from.models import upcoming
from.models import newupcoming
from.models import  newlatest
from.models import chromovies
from.models import newchromovies
# Register your models here.

class ChromoviesAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class UpcomingAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class NewlatestAdmin(admin.ModelAdmin):
    list_display = ('name','year')


class NewchromoviesAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class NewseriesAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class NewupcomingAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class NewmovieAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name','year')

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name','year')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstname','username', 'password', 'email','phonenumber')  # Customize the fields you want to display
    # Add other configurations as needed

    
admin.site.register(upcoming,UpcomingAdmin)   
admin.site.register(movie,MoviesAdmin) 
admin.site.register(series,SeriesAdmin)
admin.site.register(chromovies,ChromoviesAdmin)
admin.site.register(newlatest,NewlatestAdmin)
admin.site.register(newmovie,NewmovieAdmin)
admin.site.register(newseries,NewseriesAdmin)
admin.site.register(newupcoming,NewupcomingAdmin)
admin.site.register(newchromovies,NewchromoviesAdmin)