#cart/urls.py
from django.urls import path

from apps.cart.views import *

app_name="cart"

urlpatterns = [
    path("", cart_details, name="details"),
    path("add/<int:item_id>/", add_to_cart, name="add_to_cart"),
    path("update/<int:item_id>/", update_quantity, name="update_quantity"),
    path("remove/<int:item_id>/", remove_from_cart, name="remove_from_cart"),
    path("clear/", clear_cart, name="clear_cart")
]