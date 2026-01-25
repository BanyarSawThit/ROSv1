#orders/urls
from django.urls import path
from apps.orders import views

app_name = 'orders'

urlpatterns = [
    path("start/<str:signed_table_id>/", views.start_order, name="start"),
    path("place/", views.place_order, name='place_order'),
    path("success/", views.order_success, name='success'),
    path("history/", views.order_history, name='history')
]