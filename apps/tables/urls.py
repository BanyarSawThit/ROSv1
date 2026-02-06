# tables/urls.py

from django.urls import path
from apps.tables import views

app_name = 'tables'

urlpatterns = [
    path("<signed_table_id>/", views.start, name="start"),
]