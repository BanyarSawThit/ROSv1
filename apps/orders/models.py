from django.db import models
from apps.core.models import TimeStampedModel
from apps.tables.models import Table

class Order(TimeStampedModel):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("paid", "Paid"),
            ("preparing", "Preparing"),
            ("done", "Done"),
        ]
    )
