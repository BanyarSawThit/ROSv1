# orders/views
from decimal import Decimal

from django.shortcuts import render
from django.core import signing
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.db import transaction

from apps.cart import services as cart_services
from apps.orders.models import OrderItem, Order
from apps.tables.models import Table, DiningSession
from apps.tables.utils import validate_dining_session


@require_POST
def place_order(request):

    dining_session, redirect_response = validate_dining_session(request)
    if redirect_response:
        return redirect_response

    table_id = request.session.get('table_id')
    table = get_object_or_404(Table, id=table_id)

    summary = cart_services.cart_summary(request.session)
    items = summary['items']
    if not items:
        return redirect('cart:details')

    with transaction.atomic():
        order = Order.objects.create(
            table = table,
            dining_session = dining_session,
            status = "pending",
            total_price = Decimal("0.00")
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                item_id = item['id'],
                price = Decimal(item['price']),
                quantity = item['quantity'],
            )
        order.calculate_total()
        cart_services.delete_cart(request.session)
        request.session['last_order_id'] = order.pk

    return redirect('orders:success')


def order_success(request):
    order_id = request.session.get('last_order_id')

    if not order_id:
        return redirect('menu:list')

    order = get_object_or_404(Order, id=order_id)

    context = {
        'order': order
    }
    return render(request, 'orders/success.html', context)


def order_history(request):
    dining_session, redirect_response = validate_dining_session(request)

    if redirect_response:
        return redirect_response

    orders = (
        Order.objects
        .filter(dining_session=dining_session)
        .order_by('-created_at')
        .prefetch_related('items', 'items__item')
    )

    context = {
        'orders': orders,
    }
    return render(request, 'orders/history.html', context)