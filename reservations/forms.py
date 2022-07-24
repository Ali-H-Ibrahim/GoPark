from django.forms import Form, ModelForm, ModelChoiceField
from core.models import Reservation, Car


class ReservationChoiceField(Form):
        car = ModelChoiceField(
            queryset=Car.objects.all(), empty_label="Car", to_field_name='id'
        )

class ReservationForm(ModelForm):
    class Meta:
        model  = Reservation
        fields = (
            'car',
            'reservation_type',
            'start_date',
            'end_date',
            'cost'
        )

