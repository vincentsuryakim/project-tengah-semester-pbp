from kontak.models import Kontak
from django import forms


class KontakForm(forms.ModelForm):
    class Meta:
        model = Kontak
        fields = '__all__'
