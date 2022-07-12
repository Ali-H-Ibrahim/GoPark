from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.models import User, Park, Reservation
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
def customerReservationsPage(request, pk):
    customerReservations = Reservation.objects.filter(
        customer_id = pk
    )

    context = {'reservations': customerReservations}
    return render(request, 'admin_reservation_list.html', context)


@login_required
def addReservation(request):
    reservationForm        = ReservationForm()
    reservationChoiceField = ReservationChoiceField()

    if request.method == 'POST':
        customer = User.objects.get(id=request.POST.get('customer'))
        park     = Park.objects.get(id=request.POST.get('park'))
        
        Reservation.objects.create(
            customer         = customer,
            park             = park,
            reservation_type = request.POST.get('reservation_type'),
            reserved_period  = request.POST.get('reserved_period'),
            start_date       = request.POST.get('start_date'),
            end_date         = request.POST.get('end_date'),
            cost             = request.POST.get('cost')
        )

        # TODO set old park status to free and the new one to busy

        return redirect('show-reservations')

    context = {'form1': reservationForm, 'form2': reservationChoiceField}
    return render(request, 'admin_reservation_add.html', context)


@login_required
def updateReservation(request, pk): 
    reservation = Reservation.objects.get(id=pk)
    form1       = ReservationForm(instance=reservation) 
    form2       = ReservationChoiceField()
    
    if request.method == 'POST':
        form1    = ReservationForm(request.POST, instance=reservation)
        form2    = ReservationChoiceField(request.POST)

        if form1.is_valid() and form2.is_valid():
            form1.customer = form2.cleaned_data['customer']
            form1.park     = form2.cleaned_data['park']
            form1.save()

            # TODO set old park status to free and the new one to busy

            return redirect('show-reservations')

    context = {'form1': form1, 'form2': form2}
    return render(request, 'admin_reservation_add.html', context)


@login_required
def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)

    # TODO delete reverse scheduler task

    reservation.delete()
    return  redirect('show-reservations')