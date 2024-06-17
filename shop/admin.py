from django.contrib import admin
from .models import *


class ProductImgInline(admin.TabularInline):
    model = ImgProduct
    extra = 1
    fields = ['image']


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
