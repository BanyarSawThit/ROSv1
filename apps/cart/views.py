# cart/views
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from apps.cart import services
from apps.menu.models import MenuItem


# item names, prices, quantity, subs, totals
def cart_details(request):
    summary = services.cart_summary(request.session)
    context = {
        "cart": summary['items'],
        "total": summary['total'],
    }
    return render(request, 'cart/cart_details.html', context)


def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    services.add_item_to_cart(request.session, item)
    return redirect('menu:list')


# update qty with a new value
@require_POST
def update_quantity(request, item_id):
    quantity = int(request.POST.get("quantity", 1))
    services.update_item_quantity(request.session, item_id, quantity)
    return redirect('cart:details')


@require_POST
def remove_from_cart(request, item_id):
    services.remove_item_from_cart(request.session, item_id)
    return redirect('cart:details')


@require_POST
def clear_cart(request):
    services.delete_cart(request.session)
    return redirect('cart:details')

