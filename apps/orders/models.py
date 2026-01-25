#orders/models
from decimal import Decimal

from django.db import models

from apps.core.models import TimeStampedModel
from apps.tables.models import Table
from apps.menu.models import MenuItem


class Order(TimeStampedModel):
    objects = models.Manager()
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("paid", "Paid"),
            ("preparing", "Preparing"),
            ("done", "Done"),
        ], default="pending"
    )

    def calculate_total(self):
        self.total_price = sum(
            (item.subtotal for item in self.items.all()),
            Decimal("0.00")
        )
        self.save(update_fields=["total_price"])

    def __str__(self):
        return f"Order #{self.pk} (Table {self.table.table_number})"


class OrderItem(TimeStampedModel):
    objects = models.Manager()
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.item.name}({self.quantity})"

