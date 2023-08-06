from django import forms
from .models import BillUpload
from .models import BillParam

class BillUploadForm(forms.ModelForm):
    class Meta:
        model = BillUpload
        fields = ['bill_file']

class BillParamForm(forms.ModelForm):
    class Meta:
        model = BillParam
        fields = ['energy_contracted', 'price_per_kwh', 'mail']