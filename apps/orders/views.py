#orders/views
from django.shortcuts import render
from django.core import signing
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.db import transaction
from apps.cart import services as cart_services

from apps.cart.services import delete_cart
from apps.orders.models import OrderItem, Order
from apps.tables.models import Table
from apps.menu.models import MenuItem


def start_order(request, signed_table_id):
    data = signing.loads(signed_table_id)
    table = get_object_or_404(Table, id=data["table_id"], is_active=True)

    request.session["table_id"] = table.id
    return redirect('menu:list')


@require_POST
def place_order(request):
    table_id = request.session.get('table_id')
    table = get_object_or_404(Table, id=table_id)
    summary = cart_services.cart_summary(request.session)
    items = summary['items']

    if not items:
        return redirect('cart:details')

    with transaction.atomic():
        order = Order.objects.create(
            table = table,
            status = "pending",
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                item_id = item['id'],
                price = item['price'],
                quantity = item['quantity'],
                subtotal = item['subtotal'],
            )
        print(OrderItem.item)
        delete_cart(request.session)

    return redirect('cart:details')