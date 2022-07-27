from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParkingSerializer
from core.models import Car, Parking


@api_view(['POST'])
def addReservation(request):
    parkingSerializer = ParkingSerializer(data=request.data)

    # get user from request
    car = Car.objects.get(id=request.POST.get('car_id'))

    # TODO: Do something with car parking
       

    # calculate parking cost
    parkingCost = 20000

    # check if user is authenticated
    if user.is_authenticated:

        # check if data is valid
        if parkingSerializer.is_valid():
            
            # save reservation object
            Parking.objects.create(
                car              = car,
                # car_parking    = car_parking,
                parking_type     = 'Reserved',
                entry_date       = parkingSerializer.validated_data['entry_date'],
                end_date         = parkingSerializer.validated_data['end_date'],
                cost             = parkingCost
            )

            return Response({
                'message': 'Your reservation has been set successfully !',
            })

        return Response({'error': 'data is not valid'}, status=400)

    return Response({'error': 'user not authenticated'}, status=400)


@api_view(['POST'])
def getCarReservations(request):

    # get user from request
    user = request.user

    car = Car.objects.get(id=request.POST.get('car_id'))

    # get all car's reservations
    carReservations = Parking.objects.filter(
        car = car,
        parking_type='Reserved'
    )

    if carReservations.count() == 0:
        return Response({
            'message': 'No reservations yet'
        })
        
    serializer = ParkingSerializer(carReservations, many=True)

    return Response(serializer.data)


# TODO
@api_view(['POST'])
def updateReservation(request):
    reservationID = request.query_params['id']


@api_view(['POST'])
def deleteReservation(request):
    reservationID = request.query_params['id']

    if reservationID != None:
        reservation = Parking.objects.get(id=reservationID)
        if reservation != None:
            reservation.delete()
            return Response({
                'message': 'Deleted Successfully !'
            })

    
    return Response({   # otherwise
        'error': 'Error !'
    })


    