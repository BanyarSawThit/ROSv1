from django.contrib import admin
from apps.tables.models import Table
from apps.tables.services import generate_table_qr_code

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number", "is_active")
    actions = ["generate_qr_codes"]

    def generate_qr_codes(self, request, queryset):
        for table in queryset:
            generate_table_qr_code(table)

    generate_qr_codes.short_description = "Generate QR codes"