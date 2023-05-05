from django import forms
from .models import Gerbil


class AddGerbilForm(forms.ModelForm):
    class Meta:
        model = Gerbil
        fields = ('gerbil_name', 'gerbil_age', 'gerbil_color', 'gerbil_cage_id', 'gerbil_house_id')
