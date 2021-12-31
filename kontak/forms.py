from kontak.models import Kontak
from django import forms


class KontakForm(forms.ModelForm):
    class Meta:
        model = Kontak
        fields = [
            'nama',
            'email',
            'nomor_kontak',
        ]
