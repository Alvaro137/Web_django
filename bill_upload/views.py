# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from .forms import BillUploadForm, BillParamForm
import mimetypes
from email.mime.image import MIMEImage



def upload_bill(request):
    if request.method == 'POST':
        form_upload = BillUploadForm(request.POST, request.FILES)
        if 'upload_bill' in request.POST and form_upload.is_valid():
            form_upload.save()
            send_mail_to_alvarogil137(request.POST, request.FILES)  # Llama a la función para enviar el correo electrónico
            return redirect('bill_upload:success')
    else:
        form_upload = BillUploadForm()

    return render(request, 'bill_upload/upload_bill.html', {
        'form_upload': form_upload,
    })

def manual_input_view(request):
    if request.method == 'POST':
        form_enter_data = BillParamForm(request.POST)
        if form_enter_data.is_valid():
            form_enter_data.save()
            send_mail_to_alvarogil137(request.POST)  # Llama a la función para enviar el correo electrónico
            return redirect('bill_upload:success')
    else:
        form_enter_data = BillParamForm()

    return render(request, 'bill_upload/manual_input.html', {'form': form_enter_data})


# views.py

from django.core.mail import send_mail, EmailMessage
import mimetypes

def send_mail_to_alvarogil137(post_data, files=None):
    
    if files:
        email = EmailMessage(
            'Nueva factura introducida',
            'cuerpo',
            'alvagilsan@gmail.com',    # Remitente del correo (reemplaza con tu dirección de correo)
            ['alvarogil137@gmail.com'],   # Lista de destinatarios (puedes agregar más correos separados por comas)
        )

        for file in files.getlist('bill_file'):
            # Abre el archivo en modo binario y lee su contenido como bytes
            with file.open(mode='rb') as f:
                email.attach(file.name, f.read(), file.content_type)

        email.send()
    else:
        energy_contracted = post_data['energy_contracted']
        price_per_kwh = post_data['price_per_kwh']
        mail = post_data['mail']

        data_to_send = f"Detalles de la factura:\n" \
                   f"Contrato de energía: {energy_contracted}\n" \
                   f"Precio por kWh: {price_per_kwh}\n" \
                   f"Correo electrónico: {mail}\n" \
                   f"..."  # Personaliza según tus campos del formulario

        send_mail(
            'Nuevos datos de factura introducidos',
            data_to_send,
            'alvagilsan@gmail.com',    # Remitente del correo (reemplaza con tu dirección de correo)
            ['alvarogil137@gmail.com'],   # Lista de destinatarios (puedes agregar más correos separados por comas)
            fail_silently=False,
        )






def success(request):
    return render(request, 'bill_upload/success.html')