from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, Textarea, NumberInput, ImageField
# Same App importing
from food_items.models import FoodItems


class FoodItemsForm(forms.ModelForm):
    """Profile Creating Form """
    class Meta:
        model = FoodItems
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'category': Select(attrs={'class':'form-control'}),
            'price': NumberInput(attrs={'class':'form-control'}),
            'area': Select(attrs={'class':'form-control'}),
            'provider': Select(attrs={'class': 'form-control'}),
            'delivery_point': Select(attrs={'class': 'form-control'}),
            'minimum_quantity': NumberInput(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
            'posted_at': TextInput(attrs={'class': 'form-control'}),
        }

