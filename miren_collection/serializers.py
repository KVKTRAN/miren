from pickletools import read_long1
from unicodedata import name
from django.db import models
from rest_framework import serializers

from .models import Accessory, Bottom, Brand, Outerwear, Outfit, Shoe, Top, Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'belong_type']

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'date_found', 'image']

class OutfitDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outfit
        fields = ['id', 'name', 'description', 'concept', 'image']

class AccessoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accessory
        fields = ['id', 'name', 'description', 'brand', 'category', 'image']

class TopDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Top
        fields = ['id', 'name','description', 'pattern', 'size', 'category','image', 'brand']

####################################################
####################################################

class TopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Top
        fields = ['id', 'name','description', 'pattern', 'size', 'image', 'category', 'brand']

class BottomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bottom
        fields = ['id', 'name','description', 'pattern', 'size', 'category','image', 'brand']

class OuterwearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outerwear
        fields = ['id', 'name','description', 'pattern', 'size', 'category','image', 'brand']

class ShoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['id','description', 'pattern', 'size', 'category','image', 'brand']

class AccessorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accessory
        fields = ['id', 'name', 'description', 'brand', 'category', 'image']

####################################################
####################################################

class OutfitSerializer(serializers.HyperlinkedModelSerializer):
    tops = serializers.PrimaryKeyRelatedField(queryset=Top.objects.all(), many=True)
    accessories = serializers.PrimaryKeyRelatedField(queryset=Accessory.objects.all(), many=True)

    class Meta:
        model = Outfit
        fields = ['id', 'name', 'description', 'concept', 'image', 'shoe', 'bottom', 'outerwear', 'tops', 'accessories']

####################################################
####################################################

# List objects
###############

class ListOutfitSerializer(serializers.HyperlinkedModelSerializer):
    tops = TopDetailSerializer(many=True)
    accessories = AccessoryDetailSerializer(many=True)

    class Meta:
        model = Outfit
        fields = ['id', 'name', 'description', 'concept', 'image', 'shoe', 'bottom', 'outerwear', 'tops', 'accessories']

class ListTopSerializer(serializers.HyperlinkedModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Top
        fields = ['id', 'name','description', 'pattern', 'size', 'image', 'category', 'brand']