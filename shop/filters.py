from django import forms
from django.utils import timezone

from django.db.models import Q
from .models import *
import django_filters


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        method='filter_title',
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'style': 'padding: 5px 12px;'})
    )
    price_from = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gt',
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'style': 'padding: 5px 12px;'})
    )
    price_to = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lt',
        widget=forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md', 'style': 'padding: 5px 12px;'})
   )

    def filter_title(self, queryset, name, value):
        search_term = value
        queryset = queryset.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
        return queryset

    def filter_exclude(self, queryset, name, value):
        search_term = value
        queryset = queryset.exclude(title=search_term)
        return queryset

    class Meta:
        model = Product
        fields = ['title',
                  'price_from', 'price_to',
                  'category']
