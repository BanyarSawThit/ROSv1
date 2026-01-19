#cart/views.py
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from apps.cart.services import add_to_cart, get_cart
from apps.menu.models import MenuItem
from apps.tables.models import Table


def add_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    add_to_cart(request.session, item)
    return redirect("menu:list")

def cart_detail(request):
    cart = get_cart(request.session)
    table_id = request.session.get("table_id")

    print(cart)

    table = None
    if table_id:
        table = Table.objects.get(id=table_id)

    print(table)

    context = {
        'cart': cart,
        'table_id': table_id,
        'table': table
    }

    return render(request, 'cart/cart_details.html', context)