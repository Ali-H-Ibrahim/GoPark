from django.forms import Form, ModelForm, ModelChoiceField
from core.models import Reservation, User, Park


class ReservationChoiceField(Form):
        customer = ModelChoiceField(
            queryset=User.objects.all(), empty_label="Customer Name", to_field_name='id'
        )

        park = ModelChoiceField(
            queryset=Park.objects.filter(is_free=True), empty_label="Park Name", to_field_name='id'
        )

class ReservationForm(ModelForm):
    class Meta:
        model  = Reservation
        fields ='__all__'

