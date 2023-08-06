# bill_upload/urls.py
from django.urls import path
from . import views

app_name = 'bill_upload'

urlpatterns = [
    path('upload/', views.upload_bill, name='upload_bill'),
    path('success/', views.success, name='success'), 
    path('manual_input/', views.manual_input_view, name='manual_input'),
]
