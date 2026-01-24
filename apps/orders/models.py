#orders/models
from email.policy import default

from django.db import models
from django.shortcuts import get_object_or_404

from apps.core.models import TimeStampedModel
from apps.tables.models import Table
from apps.menu.models import MenuItem


class Order(TimeStampedModel):
    objects = models.Manager()
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("paid", "Paid"),
            ("preparing", "Preparing"),
            ("done", "Done"),
        ], default="pending"
    )

    def __str__(self):
        return f"Order #{self.pk} (Table {self.table.table_number})"


class OrderItem(TimeStampedModel):
    objects = models.Manager()
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f" {self.item.name}({self.quantity})"