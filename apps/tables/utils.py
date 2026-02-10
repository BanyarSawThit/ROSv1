# tables/utils.py

from django.shortcuts import redirect

from apps.tables.models import DiningSession

import logging

logger = logging.getLogger(__name__)

def validate_dining_session(request, redirect_url='tables:no_session'):
    dining_session_id = request.session.get('dining_session_id')
    logger.debug(f"id: {dining_session_id}")

    if not dining_session_id:
        return None, redirect(redirect_url)

    try:
        dining_session = DiningSession.objects.get(
            id=dining_session_id,
            is_active=True
        )
        return dining_session, None
    except DiningSession.DoesNotExist:
        return None, redirect(redirect_url)