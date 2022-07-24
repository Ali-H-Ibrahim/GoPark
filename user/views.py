from django.shortcuts import render

# from django.contrib.auth.models import User


from django.shortcuts import render, redirect, reverse
from . import models
from django.contrib.auth.models import Group
from django.db.models import Sum
from django.db.models import Q
from django.http import HttpResponseRedirect

from core import models
from django.contrib.auth.hashers import make_password
from django.contrib import messages




# Create your views here.

def manage_users(request):
    return render(request, 'admin_customer.html')



def users_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' 

    customers = models.User.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q)  |
        Q(email__icontains=q)
    )

    # calculate customer cars count and customer reservations count

    customerCarsCount = []
    # customerRservationsCount = []

    for customer in customers:
        customerCarsCount.append(models.Car.objects.filter(
            owner_id = customer.id
        ).count())

    #     customerRservationsCount.append(models.Reservation.objects.filter(
    #         customer_id = customer.id
    #     ).count())        
    

    # TODO : calculate customer total payments


    # packing all three lists
    customerInfo = zip(customers, customerCarsCount)

    return render(request, 'admin_view_customer.html', {'customerInfo': customerInfo})


def add_user(request):
    choice = ['1', '0', 5000, 10000, 15000, 'Register', 'Admin', 'Cashier']
    choice = {'choice': choice}
    if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            phone_number =request.POST['phone_number']
            userType=request.POST['userType']
            email=request.POST['email']
            password=request.POST['password']
            password = make_password(password)
            print("User Type"+userType)
            print(userType)
            if userType == "Cashier":
                a = models.User(permission=userType, first_name=first_name, last_name=last_name, phone_number=phone_number, username=username, email=email, password=password)
                a.save()
                messages.success(request, 'Member was created successfully!')
                return redirect('manage-users')
            elif userType == "Admin":
                a = models.User(permission=userType, first_name=first_name, last_name=last_name, phone_number=phone_number, username=username, email=email, password=password)
                a.save()
                messages.success(request, 'Member was created successfully!')
                return redirect('manage-users') 
            else:
                messages.success(request, 'Member was not created')
                return redirect('manage-users')
    else:
        choice = ['1', '0', 5000, 10000, 15000, 'Register', 'Admin', 'Cashier']
        choice = {'choice': choice}
        return render(request, 'admin_add_customer.html', choice)


def delete_user(request, pk):
    user = models.User.objects.get(id=pk)
    user.delete()
    return redirect('users-view')    



def update_user(request, pk):
    choice = ['1', '0', 5000, 10000, 15000, 'Register', 'Admin', 'Cashier']
    choice = {'choice': choice}
    user = models.User.objects.get(id=pk)

    if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            phone_number =request.POST['phone_number']
            userType=request.POST['permission']
            email=request.POST['email']
            password=request.POST['password']
            password = make_password(password)
            print("User Type"+userType)
            print(userType)

            user.permission=userType
            user.first_name=first_name
            user. last_name=last_name 
            user.phone_number=phone_number
            user.username=username
            user.email=email
            user.password=password
            user.save()
            messages.success(request, 'Member was created successfully!')
            return redirect('users-view') 
    data = {'choice': choice , 'user':user}

    return render(request, 'update_user.html',data )    


def admin_view_customer_invoice_view(request):
    return render(request, 'admin_view_customer_invoice.html', {})


def admin_view_customer_enquiry_view(request):
    return render(request, 'admin_view_customer_enquiry.html', {})