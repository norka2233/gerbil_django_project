from django import forms
from .models import Gerbil


class AddGerbilForm(forms.ModelForm):
    class Meta:
        model = Gerbil
        fields = ('gerbil_name', 'gerbil_id', 'gerbil_age', 'gerbil_color', 'gerbil_cage_id', 'gerbil_house_id')
        # labels = {'gerbil_name': "name", 'gerbil_id': 5, 'gerbil_age': 2, 'gerbil_color': 'gr', 'gerbil_cage_id': 1, 'gerbil_house_id': 1}
    # gerbil_name = forms.CharField(widget=forms.TextInput, max_length=100)

# gerbil = AddGerbilForm()
# gerbil.objects.get(pk=1)
# class AddGerbilForm(forms.Form):
#     gerbil_name = forms.CharField(label="gerbil_name", max_length=100)

# class CreateBookForm(forms.ModelForm):
#
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#
#         model = Book
#         fields = ('name', 'description', 'count', 'authors')