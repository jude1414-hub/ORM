# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books
### ENTITY RELATIONSHIP DIAGRAM:
![alt text](<Screenshot 2025-05-09 165754.png>)
## PROGRAM
~~~
models.py

from django.db import models
from django.contrib import admin

class Movies(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)

class MoviesAdmin(admin.ModelAdmin):
    list_display=('title','year','rating','genre')

admins.py

from django.contrib import admin
from .models import Movies,MoviesAdmin
admin.site.register(Movies,MoviesAdmin)
~~~
## OUTPUT

Include the screenshot of your admin page.
![alt text](<Screenshot 2025-05-02 180114.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
