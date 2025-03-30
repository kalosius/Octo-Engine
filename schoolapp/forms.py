from django import forms
from .models import SeniorOne

class SeniorOneForm(forms.ModelForm):
    class Meta:
        model = SeniorOne
        fields = '__all__'