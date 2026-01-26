#tables/models
from django.utils import timezone
from django.db import models

from apps.core.models import TimeStampedModel


class Table(TimeStampedModel):
    objects = models.Manager()
    table_number = models.PositiveIntegerField(unique=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"


class DinningSession(TimeStampedModel):
    objects = models.Manager()
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    paid_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def close(self):
        self.is_active = False
        self.paid_at = timezone.now()
        self.save(update_fields=['is_active', 'paid_at'])