from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields import DecimalField
from django.db.models.fields import EmailField
from django.db.models.fields.files import FileField


class BillParam(models.Model):
    energy_contracted = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_kwh = models.DecimalField(max_digits=8, decimal_places=4)
    mail = models.EmailField(default='default@example.com')  # Agrega el campo 'mail' con un valor predeterminado

    def __str__(self):
        return f"Parámetros de Factura de {self.mail}"


class BillUpload(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    bill_file = models.FileField(upload_to="")  # Cambia "bill_uploads/" por la ruta deseada para guardar las facturas

    def __str__(self):
        return f"{self.upload_date}"

