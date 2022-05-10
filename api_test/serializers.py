from pyexpat import model
from attr import field
from django.db import models
from rest_framework import serializers

from .models import API_Brand, Author, Book, Meal

class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Meal
        fields = ['id', 'name','description', 'image']

class APIBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = API_Brand
        fields = ['id', 'name', 'date_found', 'logo']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'published')

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name')

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    # authors = AuthorDetailSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'published', 'authors')
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)
    # books = BookDetailSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name', 'books')
        
class ListBookSerializer(serializers.ModelSerializer):
    # authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    authors = AuthorDetailSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'published', 'authors')
        depth = 1