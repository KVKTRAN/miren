from django import urls
from django.urls import path, include
from rest_framework import routers, urlpatterns
import rest_framework

from . import views

router = routers.DefaultRouter()
router.register(r'tops', views.TopViewSet)
router.register(r'bottoms', views.BottomViewSet)
router.register(r'outerwears', views.OuterwearViewSet)
router.register(r'shoes', views.ShoesViewSet)
router.register(r'outfits', views.OutfitViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'accessories', views.AccessoryViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]