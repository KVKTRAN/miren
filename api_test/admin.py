from django.contrib import admin
from .models import Author, Book, Meal
# Register your models here.

admin.site.register(Meal)
admin.site.register(Author)
admin.site.register(Book)