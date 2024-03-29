from django import forms
from .models import Cage


class AddCageForm(forms.ModelForm):
    class Meta:
        model = Cage
        fields = ('cage_capacity', 'cage_material', 'cage_color', 'gerbil_house_id')
