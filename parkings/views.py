from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import CarParkingSerializer
from core.models import Car, CarParking, Park, Brand


@api_view(['POST'])
def addCarParking(request):
    plateNumber = request.POST.get('plateNumber')
    car = Car.objects.get(plateNumber=plateNumber)

    # if car.count() == 1:    # means the car is already existed in the DB
    #     carParkingSerializer = CarParkingSerializer(data=request.data)
    #     if carParkingSerializer.is_valid():
    #         park = Park.objects.get(is_free=True)   # find a park
    #         CarParking.objects.create(
    #             car        = car,
    #             park       = park,
    #         )
    #         return Response(
    #             'Parking has been set successfully !'
    #         )

    # else:   # the car is not registered
    #     # brand = Brand.objects.get(
    #     #     name = request.POST.get('brand')
    #     # )
    #     # Car.objects.create(

    #     # )
    #     return Response(
    #         'hey'
    #     )

    