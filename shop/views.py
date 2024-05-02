from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .filters import ProductFilter


def home(request):
    context = {}
    context['categories'] = Category.objects.all()
    context['product_hit'] = Product.objects.all().order_by('?')[:4]
    context['product_rec'] = Product.objects.all().order_by('?')[:4]
    return render(request, 'index.html', context)


def products(request):
    context = {}
    context['categories'] = Category.objects.all()
    return render(request, 'products.html', context)


class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products.html'
    context_object_name = 'products'
    filter_class = ProductFilter
    paginate_by = 10

    def get_queryset(self):
        query = self.queryset
        filter = self.filter_class(self.request.GET, queryset=query)
        query = filter.qs
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['filter'] = ProductFilter(self.request.GET).form
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'productDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET).form
        context['categories'] = Category.objects.all()
        return context
