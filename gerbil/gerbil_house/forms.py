from django import forms
from .models import House


class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('house_capacity', 'house_material', 'house_color')