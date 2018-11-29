from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, Textarea, NumberInput
# Same App importing
from food_order.models import Order


class OrderForm(forms.ModelForm):
    """Profile Creating Form """
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'client_info': Select(attrs={'class': 'form-control'}),
            'food_name': Select(attrs={'class': 'form-control'}),
            'provider': Select(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'delivery_point': Select(attrs={'class': 'form-control'}),
            'area': Select(attrs={'class': 'form-control'}),
        }

