from rest_framework.serializers import ModelSerializer
from core.models import Reservation

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'reservation_type',
            'reserved_period',
            'start_date',
            'end_date',
        )