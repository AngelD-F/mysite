from django import forms

from .models import order

class orderForm(forms.ModelForm):
    class Meta():
        model = order
        fields = '__all__'
