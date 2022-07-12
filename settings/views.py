import email
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Setting
from .forms import SettingsForm

def site_settings(request):
    settings = Setting.objects.first()
    settingsForm = SettingsForm()

    if request.method == 'POST':        
        Setting.objects.update(
            name    = request.POST.get('name'),
            email   = request.POST.get('email'),
            phone   = request.POST.get('phone'),
            address = request.POST.get('address'),
        )

        return redirect(reverse('settings:site-settings'))

    context = {'form': settingsForm, 'settings': settings}
    return render(request, 'admin_settings.html', context)