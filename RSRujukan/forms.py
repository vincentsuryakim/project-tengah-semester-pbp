from django import forms
from django.forms import widgets
from .models import BookingRS, RumahSakit

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRS
        fields = [
            'nama',
            'umur',
            'noTelfon',
            'rumahSakit',
        ]
        labels ={
            'nama' : 'Nama',
            'umur' : 'Umur',
            'noTelfon' : 'Nomor Telfon',
            'rumahSakit' : 'Rumah Sakit'
        }
        widgets = {
            'nama' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan nama..'}),
            'umur' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan umur..'}),
            'noTelfon' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan nomor telfon..'}),
        }

class AddRS(forms.ModelForm):
    class Meta:
        model = RumahSakit
        fields = [
            'nama',
            'tempat',
            'alamat',
            'no_telfon',
        ]
        labels ={
            'nama' : 'Nama',
            'tempat' : 'Tempat',
            'alamat' : 'Alamat',
            'no_telfon' : 'Nomor Telfon'
        }
        widgets = {
            'nama' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan nama..'}),
            'alamat' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan alamat'}),
            'no_telfon' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Masukkan nomor telfon..'}),
        }