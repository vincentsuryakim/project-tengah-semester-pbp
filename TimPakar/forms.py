from django import forms
from django.forms import ModelForm
from TimPakar.models import Regist

class RegistForm(ModelForm):
    class Meta:
        model = Regist
        fields = ['nama', 'asalUniversitas', 'tempatBertugas', 'pesan']

    error_messages = {
        'required' : 'Harap isi semua data'
    }

    input_attrs = {
        'type' : 'text',
    }

    nama = forms.CharField(label="nama", required=True, max_length=30, widget=forms.TextInput(attrs=input_attrs), error_messages=error_messages)
    asalUniversitas = forms.CharField(label="asalUniversitas", required=True, max_length=30, widget=forms.TextInput(attrs=input_attrs), error_messages=error_messages)
    tempatBertugas = forms.CharField(label="tempatBertugas", required=True, max_length=30, widget=forms.TextInput(attrs=input_attrs), error_messages=error_messages)
    pesan = forms.CharField(label="pesan", required=True, widget=forms.Textarea(attrs=input_attrs), error_messages=error_messages)