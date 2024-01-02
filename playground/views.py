from django.shortcuts import render
from django.db.models import Value, F, ExpressionWrapper, DecimalField

from store.models import Product, Customer


def say_hello(request):
    # queryset = Product.objects.order_by('-title')
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price=discounted_price
    )

    
    return render(request, 'hello.html', {'products': queryset})