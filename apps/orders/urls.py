#orders/urls
from django.urls import path
from apps.orders import views

app_name = 'orders'

urlpatterns = [
    path("place/", views.place_order, name='place_order'),
    path("success/", views.order_success, name='success'),
    path("history/", views.order_history, name='history')
]