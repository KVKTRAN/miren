from distutils.command.upload import upload
from pyexpat import model
from sys import path
from unicodedata import name
from django.db import models
from django.utils import timezone
import os
from uuid import uuid4

def path_and_rename(instance, filename, directory):
    upload_to = directory
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

def top_rename(instance, filename):
    return path_and_rename(instance, filename, directory='tops')

def bot_rename(instance, filename):
    return path_and_rename(instance, filename, directory='bottoms')

def outerwear_rename(instance, filename):
    return path_and_rename(instance, filename, directory='outerwears')

def accessory_rename(instance, filename):
    return path_and_rename(instance, filename, directory='accessories')

def hat_rename(instance, filename):
    return path_and_rename(instance, filename, directory='hats')

def shoes_rename(instance, filename):
    return path_and_rename(instance, filename, directory='shoes')

def brand_rename(instance, filename):
    return path_and_rename(instance, filename, directory='brands')

    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    belong_type = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    date_found = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=brand_rename, null=True, blank=True)

    def __str__(self):
        return self.name

class Top(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pattern = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=top_rename)

    def __str__(self):
        return self.name

class Bottom(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    pattern = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=bot_rename, null=True, blank=True)

    def __str__(self):
        return self.name

class Outerwear(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    pattern = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=outerwear_rename, null=True, blank=True)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    description = models.CharField(max_length=200)
    pattern = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=shoes_rename, null=True, blank=True)

    def __str__(self):
        return self.category.name

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=accessory_rename, null=True, blank=True)

    def __str__(self):
        return self.name
        
class Outfit(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    concept = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=shoes_rename, null=True, blank=True)
    
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, null=True, blank=True)
    bottom = models.ForeignKey(Bottom, on_delete=models.CASCADE, null=True, blank=True)
    outerwear = models.ForeignKey(Outerwear, on_delete=models.CASCADE, null=True, blank=True)
    
    tops = models.ManyToManyField(Top, related_name="outfits", blank=True)
    accessories = models.ManyToManyField(Accessory, related_name='outfits', blank=True)

    def __str__(self):
        return self.name