from django import forms
from .models import musician

class add_musician(forms.ModelForm):
    class Meta:
        model=musician
        fields='__all__'
