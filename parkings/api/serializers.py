from rest_framework.serializers import ModelSerializer
from core.models import Parking

class ParkingSerializer(ModelSerializer):
    class Meta:
        model = Parking
        fields = (
            'id',
            'parking_type',
            'start_date',
            'end_date',
            'cost'
        )