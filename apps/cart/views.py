#cart/views.py
from django.shortcuts import render, redirect
from apps.cart.services import add_to_cart, get_cart
from apps.menu.models import MenuItem

def add_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    add_to_cart(request.session, item)
    return redirect("menu:list")

def cart_detail(request):
    cart = get_cart(request.session)

    context = {
        'cart': cart,
    }

    return render(request, 'cart/cart_details.html', context)