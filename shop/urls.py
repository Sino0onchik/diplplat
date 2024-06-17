from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('order/create/<int:pk>', order_create, name='order_create'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
