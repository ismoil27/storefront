from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Cart,CartItem
from tags.models import TaggedItem


def say_hello(request):

    # Creating a shopping cart with an item
    cart = Cart()
    cart.save()


    item1 = CartItem()
    item1.cart = cart
    item1.product_id = 1
    item1.quantity = 1
    item1.save()

# Updating the quantity of an item
    item1 = CartItem.objects.get(pk=1)
    item1.quantity = 2
    item1.save()


    # Removing a cart
    cart = Cart(pk=1)
    cart.delete()
    

    return render(request, 'hello.html', {'name': 'Jon'})