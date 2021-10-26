from django import forms
from .models import Sebaran

class SebaranForm(forms.ModelForm):
    class Meta:
        model = Sebaran
        fields = "__all__"