from unicodedata import name
from urllib import response
from django.shortcuts import render
from html5lib import serialize

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.response import Response 

from .serializers import AuthorSerializer, BookSerializer, MealSerializer, ListBookSerializer
from .models import Author, Book, Meal
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


######################################
# Filter objects                     #
######################################

class BookFilter(django_filters.FilterSet):
    authors = django_filters.Filter(method='my_custom_filter')

    class Meta:
        model = Book
        fields = ['authors']

    def my_custom_filter(self, queryset, author, value):
        return queryset.filter(**{
            author: value,
        })

######################################
# View objects                       #
######################################


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['authors']
    search_fields = ['name']

    def get_queryset(self):
        query_set = Book.objects.all()
        authors = self.request.query_params.getlist('authors')
        for author in authors:
            query_set = query_set.filter(authors__id__contains=author)
        return query_set.distinct()

    def list(self, request, *args, **kwargs):
        serializer = ListBookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        new_book = Book.objects.create(name=data['name'], published=data['published'])
        new_book.save()

        for author in data['authors']:
            m_author = Author.objects.get(id=author)
            new_book.authors.add(m_author)

        serializer = BookSerializer(new_book)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data 
        m_book = Book.objects.get(id=data['id'])
        for key, value in data.items():
            if key == 'authors':
                continue
            setattr(m_book, key, value)
        m_book.save()

        for author in data['authors']:
            m_author = Author.objects.get(id=author)
            m_book.authors.add(m_author)

        serializer = BookSerializer(m_book)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']

    def create(self, request, *args, **kwargs):
        data = request.data 
        new_author = Author.objects.create(name=data['name'], last_name=data['last_name'])
        new_author.save()

        for book in data['books']:
            m_book = Book.objects.get(id=book)
            new_author.books.add(m_book)

        serializer = AuthorSerializer(new_author)
        return Response(serializer.data)