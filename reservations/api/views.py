from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from .serializers import ReservationSerializer
from core.models import Park, Reservation


@api_view(['POST'])
def addReservation(request):
    reservationSerializer = ReservationSerializer(data=request.data)

    # get user from request
    user = request.user

    # find a free park
    park = Park.objects.filter(is_free=True)
    
    # calculate parking cost
    parkingCost = 20000

    # check if user is authenticated
    if user.is_authenticated:

        # check if data is valid
        if reservationSerializer.is_valid():
            
            # save reservation object
            Reservation.objects.create(
                customer         = user,
                park             = park[0],
                reservation_type = reservationSerializer.validated_data['reservation_type'],
                reserved_period  = reservationSerializer.validated_data['reserved_period'],
                start_date       = reservationSerializer.validated_data['start_date'],
                end_date         = reservationSerializer.validated_data['end_date'],
                cost             = parkingCost
            )

            return Response({
                'message': 'Your reservation has been set successfully !',
                'park': str(park[0])
            })

        return Response({'error': 'data is not valid'}, status=400)

    return Response({'error': 'user not authenticated'}, status=400)