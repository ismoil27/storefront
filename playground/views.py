from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum 
from store.models import Product, OrderItem, Order


def say_hello(request):
    # queryset = Product.objects.order_by('-title')
    queryset = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    
    return render(request, 'hello.html', {'products': queryset})