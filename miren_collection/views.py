from unicodedata import category
from urllib import response
from winreg import QueryValueEx
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import filters

from .serializers import AccessorySerializer, BottomSerializer, BrandSerializer, CategorySerializer, ListTopSerializer, TopDetailSerializer
from .serializers import ListOutfitSerializer, OuterwearSerializer, OutfitSerializer, ShoesSerializer, TopSerializer
from .models import Accessory, Bottom, Brand, Category, Outerwear, Outfit, Shoe, Top

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'belong_type']

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

####################################################
####################################################

class TopViewSet(viewsets.ModelViewSet):
    queryset = Top.objects.all().order_by('name')
    serializer_class = TopSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        query_set = Top.objects.all()
        name = self.request.query_params.get('search')
        if name is not None:
            query_set = query_set.filter(name__contains=name)
        return query_set

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListTopSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class BottomViewSet(viewsets.ModelViewSet): 
    queryset = Bottom.objects.all().order_by('name')  
    serializer_class = BottomSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['pattern', 'category', 'brand']
    search_fields = ['name', 'brand']


class OuterwearViewSet(viewsets.ModelViewSet):
    queryset = Outerwear.objects.all().order_by('name')
    serializer_class = OuterwearSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['pattern', 'category', 'brand']
    search_fields = ['name', 'brand']


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all().order_by('id')
    serializer_class = ShoesSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand']
    search_fields = ['category']

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all().order_by('name')
    serializer_class = AccessorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['brand', 'category']

####################################################
####################################################


class OutfitViewSet(viewsets.ModelViewSet):
    queryset = Outfit.objects.all().order_by('name')
    serializer_class = OutfitSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]

    def list(self, request, *args, **kwargs):
        queryset = Outfit.objects.all()
        serializer = ListOutfitSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)