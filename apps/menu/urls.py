from django.urls import path, include
from apps.menu.views import MenuListView

app_name = 'menu'

urlpatterns = [
    path("", MenuListView.as_view(), name="list"),
]