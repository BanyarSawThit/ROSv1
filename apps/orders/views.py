from django.shortcuts import render
from django.core import signing
from django.shortcuts import get_object_or_404, redirect
from apps.tables.models import Table

# Create your views here.
def start_order(request, signed_table_id):
    data = signing.loads(signed_table_id)
    table = get_object_or_404(Table, id=data["table_id"], is_active=True)

    request.session["table_id"] = table.id
    return redirect("menu:list")