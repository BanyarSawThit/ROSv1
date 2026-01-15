from django.db import models

from apps.core.models import TimeStampedModel


class Table(TimeStampedModel):
    table_number = models.PositiveIntegerField(unique=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True)
    is_active = models.BooleanField(default=True)
