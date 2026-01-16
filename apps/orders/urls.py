from django.urls import path
from apps.orders.views import start_order

app_name = 'orders'

urlpatterns = [
    path("start/<str:signed_table_id>/", start_order, name="start"),
]