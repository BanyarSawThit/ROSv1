import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.urls import reverse
from django.conf import settings
from django.core import signing

def generate_table_qr_code(table):
    signed_table_id = signing.dumps({"table_id": table.id})

    path=reverse("orders:start", args=[signed_table_id])
    print(path)
    qr_url = f"{settings.SITE_URL}{path}"
    print(qr_url)

    qr = qrcode.make(qr_url)
    buffer = BytesIO()
    print(buffer)
    qr.save(buffer, format="PNG")

    filename = f"table_{table.table_number}_qr.png"
    table.qr_code.save(
        filename,
        ContentFile(buffer.getvalue()),
        save=True
    )
