from django.contrib import admin

from .models import Accessory, Bottom, Brand, Category, Outerwear, Outfit, Shoe, Top

# Register your models here.
admin.site.register(Top)
admin.site.register(Bottom)
admin.site.register(Shoe)
admin.site.register(Outerwear)
admin.site.register(Brand)
admin.site.register(Outfit)
admin.site.register(Category)
admin.site.register(Accessory)