#cart/urls.py
from django.urls import path
from apps.cart.views import add_item, cart_detail

app_name="cart"

urlpatterns = [
    path("", cart_detail, name='details'),
    path("<int:item_id>/", add_item, name="add_item"),
]