from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.models import Car, Reservation
from .forms import ReservationForm, ReservationChoiceField
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def reservations_main(request):
    context = {}
    return render(request, 'admin_reservation_home.html', context)


@login_required
def showReservations(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''    # filtering value (YYYY-MM-DD)

    reservations = Reservation.objects.filter(
        Q(start_date__date__contains=q) 
    )

    context = {'reservations': reservations}
    return render(request, 'admin_reservation_list.html', context)


@login_required
def carReservationsPage(request, pk):
    carReservations = Reservation.objects.filter(
        car_id = pk
    )

    context = {'reservations': customerReservations}
    return render(request, 'admin_reservation_list.html', context)


@login_required
def addReservation(request):
    reservationForm        = ReservationForm()
    reservationChoiceField = ReservationChoiceField()

    if request.method == 'POST':
        car  = Car.objects.get(id=request.POST.get('car'))
        # TODO: Do something with car parking
        # car_parking = car_parking.objects.create(

        # )
        
        Reservation.objects.create(
            car              = car,
            # car_parking      = car_parking,
            reservation_type = request.POST.get('reservation_type'),
            start_date       = request.POST.get('start_date'),
            end_date         = request.POST.get('end_date'),
            cost             = request.POST.get('cost')
        )

        return redirect('show-reservations')

    context = {'form1': reservationForm, 'form2': reservationChoiceField}
    return render(request, 'admin_reservation_add.html', context)


@login_required
def updateReservation(request, pk): 
    reservation = Reservation.objects.get(id=pk)
    form1       = ReservationForm(instance=reservation) 
    form2       = ReservationChoiceField()
    
    if request.method == 'POST':
        form1 = ReservationForm(request.POST, instance=reservation)
        form2 = ReservationChoiceField(request.POST)

        if form1.is_valid() and form2.is_valid():
            form1.car = form2.cleaned_data['car']
            form1.save()

            return redirect('show-reservations')

    context = {'form1': form1, 'form2': form2}
    return render(request, 'admin_reservation_add.html', context)


@login_required
def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)

    # TODO delete reverse scheduler task

    reservation.delete()
    return  redirect('show-reservations')