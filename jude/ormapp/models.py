from django.db import models
from django.contrib import admin

class Movies(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)

class MoviesAdmin(admin.ModelAdmin):
    list_display=('title','year','rating','genre')