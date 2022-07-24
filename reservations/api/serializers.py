from rest_framework.serializers import ModelSerializer
from core.models import Reservation

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'id',
            'reservation_type',
            'start_date',
            'end_date',
            'cost'
        )