from distutils.command.upload import upload
from pyexpat import model
from sys import path
from unicodedata import name
from django.db import models
from django.utils import timezone
import os
from uuid import uuid4

import django_filters

def path_and_rename(instance, filename, directory):
    upload_to = directory
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

def brand_rename(instance, filename):
    return path_and_rename(instance, filename, directory='api_brands')

def meal_rename(instance, filename):
    return path_and_rename(instance, filename, directory='meals')

class API_Brand(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    date_found = models.DateField(null=True, blank=True)

    logo = models.ImageField(upload_to=brand_rename, null=True, blank=True)

    def __str__(self):
        return self.name



# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to=meal_rename)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    last_name = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Book(models.Model):
    authors = models.ManyToManyField(Author, related_name="books", blank=True)
    name = models.CharField(max_length=100, default="")
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name