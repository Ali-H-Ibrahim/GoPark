from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.db.models import Q
from django.http import HttpResponseRedirect
from core import models
from feedbacks.models import Feedback


# ============================================================================================
# ADMIN RELATED views start
# ============================================================================================

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('admin-dashboard')

    email    = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(request, email=email, password=password)
    
    login(request, user)

    return HttpResponseRedirect('admin-dashboard')


def afterlogin_view(request):
    return redirect('admin-dashboard')


# @login_required(login_url='adminlogin')
def admin_dashboard_view(request):

    dict = {
        'total_customers': models.User.objects.all().count(),
        'total_cars': models.Car.objects.all().count(),
        'total_incomes': 10, 
        'total_feedback': Feedback.objects.all().count(),
        'total_reservations': models.Reservation.objects.all().count(),
        'total_employees': 10, 
        'total_parks': models.Park.objects.all().count(),
        'available_parks': models.Park.objects.filter(is_free=True).count(),
        'data': zip([10], [10]),
    }

    return render(request, 'vehicle/admin_dashboard.html', context=dict)


def admin_report_view(request):
    dict = {}
    return render(request, 'vehicle/admin_report.html', context=dict)


def admin_feedback_view(request):
    return render(request, 'vehicle/admin_feedback.html', {})


def logoutUser(request):
    logout(request)
    return render(request, 'vehicle/adminlogin.html')
