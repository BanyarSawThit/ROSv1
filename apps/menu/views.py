from django.shortcuts import render
from django.views.generic import ListView

from .models import MenuItem

class MenuListView(ListView):
    model = MenuItem
    template_name = "menu/menu_page.html"
    context_object_name = "items"

    def get_queryset(self):
        return MenuItem.objects.filter(is_available=True)

def MenuView(request):
    model = MenuItem.objects.filter(is_available=True)