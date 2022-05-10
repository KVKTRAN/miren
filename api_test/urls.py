from django import urls
from django.urls import path, include
from rest_framework import routers, urlpatterns
import rest_framework

from . import views

router = routers.DefaultRouter()
# can not add generic view in router object
router.register(r'meals', views.MealViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('accessories/', views.AccessoryList.as_view(), name='accessories'),
    path('api-auth/', include('rest_framework.urls', namespace='api_test'))
]