from django import forms
from django.contrib.auth.models import User
from core.models import Car, CarParking, Brand, User


class AdminCarAddForm(forms.Form):
    owner = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Owner Name", to_field_name='id'
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(), empty_label="Brand Name", to_field_name='id'
    )

class CarForm(forms.ModelForm):
    class Meta:
        model   = Car
        fields  = '__all__'
        widgets = { }