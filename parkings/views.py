from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.models import Car, Parking, Floor
from .forms import ParkingForm, ParkingChoiceField
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from settings.models import Setting


@login_required
def parkings_main(request):
    context = {}
    return render(request, 'parkings_home.html', context)


@login_required
def showParkings(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''    # filtering value (YYYY-MM-DD)

    parkings = Parking.objects.filter(
        Q(entry_date__contains=q) 
    )

    context = {'parkings': parkings}
    return render(request, 'parkings_list.html', context)


@login_required
def carParkingsPage(request, pk):
    carParkings = Parking.objects.filter(
        car_id = pk
    )

    context = {'parkings': carParkings}
    return render(request, 'parkings_list.html', context)


@login_required
def addParking(request):
    parkingForm        = ParkingForm()
    parkingChoiceField = ParkingChoiceField()

    if request.method == 'POST':
        form1 = ParkingForm(request.POST)
        form2 = ParkingChoiceField(request.POST)

        if form1.is_valid() and form2.is_valid():
            form1.car   = form2.cleaned_data['car']
            form1.floor = form2.cleaned_data['floor'] 
            parking = form1.save(commit=False)
            
            # calculate parking cost
            parked_hours   = form1.cleaned_data['end_time'].hour - form1.cleaned_data['entry_time'].hour
            parked_minutes = form1.cleaned_data['end_time'].minute - form1.cleaned_data['entry_time'].minute
            parked_time = parked_hours + parked_minutes / 60
            parking.cost = parked_time * Setting.objects.first().hourly_cost
            parking.save()

            parking.floor.busy_parks += 1
            if parking.floor.busy_parks == parking.floor.num_of_parks:
                parking.floor.is_free = False
            parking.floor.save()

            return redirect('show-parkings')

    context = {'form1': parkingForm, 'form2': parkingChoiceField}
    return render(request, 'parkings_add.html', context)


@login_required
def updateParking(request, pk): 
    parking = Parking.objects.get(id=pk)
    if request.method != 'POST':
        parking.floor.busy_parks -= 1
        parking.floor.save()

    form1       = ParkingForm(instance=parking) 
    form2       = ParkingChoiceField()
    
    if request.method == 'POST':
        form1 = ParkingForm(request.POST, instance=parking)
        form2 = ParkingChoiceField(request.POST)

        if form1.is_valid() and form2.is_valid():
            form1.car   = form2.cleaned_data['car']
            form1.floor = form2.cleaned_data['floor']
            parking = form1.save(commit=False)
            
            # calculate parking cost
            parked_hours   = form1.cleaned_data['end_time'].hour - form1.cleaned_data['entry_time'].hour
            parked_minutes = form1.cleaned_data['end_time'].minute - form1.cleaned_data['entry_time'].minute
            parked_time = parked_hours + parked_minutes / 60
            parking.cost = parked_time * Setting.objects.first().hourly_cost
            parking.save()

            parking.floor.busy_parks += 1
            if parking.floor.busy_parks == parking.floor.num_of_parks:
                parking.floor.is_free = False
            parking.floor.save()

            return redirect('show-parkings')

    context = {'form1': form1, 'form2': form2}
    return render(request, 'parkings_add.html', context)


@login_required
def deleteParking(request, pk):
    parking = Parking.objects.get(id=pk)

    parking.floor.busy_parks -= 1
    parking.floor.save()    

    parking.delete()
    return  redirect('show-parkings')