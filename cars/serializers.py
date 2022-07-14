from rest_framework.serializers import ModelSerializer
from core.models import Car, CarParking


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarParkingSerializer(ModelSerializer):
    class Meta:
        model = CarParking
        fields = '__all__'

