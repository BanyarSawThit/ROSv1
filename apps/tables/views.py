# tables/views.py

from django.core import signing
from django.shortcuts import render, get_object_or_404, redirect

from apps.tables.models import Table, DiningSession


# Create your views here.

def start(request, signed_table_id):
    data = signing.loads(signed_table_id)
    table = get_object_or_404(Table, id=data['table_id'], is_active=True)

    dining_session = DiningSession.objects.filter(
        table = table,
        is_active = True
    ).first()

    if not dining_session:
        dining_session = DiningSession.objects.create(
            table = table
        )

    request.session['dining_session_id'] = dining_session.id
    request.session['table_id'] = table.id
    return redirect('menu:list')


def no_session(request):
    return render(request, 'tables/doest_not_exist_or_expired.html')