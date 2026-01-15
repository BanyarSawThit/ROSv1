from django.contrib import admin
from apps.menu.models import Category, MenuItem

admin.site.register((Category, MenuItem))