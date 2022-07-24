from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReservationSerializer
from core.models import Car, CarParking, Reservation


@api_view(['POST'])
def addReservation(request):
    reservationSerializer = ReservationSerializer(data=request.data)

    # get user from request
    car = Car.objects.get(id=request.POST.get('car_id'))

    # TODO: Do something with car parking
        # car_parking = car_parking.objects.create(

        # )

    # calculate parking cost
    parkingCost = 20000

    # check if user is authenticated
    if user.is_authenticated:

        # check if data is valid
        if reservationSerializer.is_valid():
            
            # save reservation object
            Reservation.objects.create(
                car              = car,
                # car_parking     = car_parking,
                reservation_type = reservationSerializer.validated_data['reservation_type'],
                start_date       = reservationSerializer.validated_data['start_date'],
                end_date         = reservationSerializer.validated_data['end_date'],
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
    carReservations = Reservation.objects.filter(
        car = car
    )

    if carReservations.count() == 0:
        return Response({
            'message': 'No reservations yet'
        })
        
    serializer = ReservationSerializer(carReservations, many=True)

    return Response(serializer.data)


# TODO
@api_view(['POST'])
def updateReservation(request):
    reservationID = request.query_params['id']


@api_view(['POST'])
def deleteReservation(request):
    reservationID = request.query_params['id']

    if reservationID != None:
        reservation = Reservation.objects.get(id=reservationID)
        if reservation != None:
            reservation.delete()
            return Response({
                'message': 'Deleted Successfully !'
            })

    
    return Response({   # otherwise
        'error': 'Error !'
    })


    