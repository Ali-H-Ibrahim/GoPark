from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('reserve/', include('reservations.urls')),
    path('cars/', include('cars.urls')),
    path('users/', include('user.urls')),
    path('settings/', include('settings.urls')),
    path('feedbacks/', include('feedbacks.urls'))
]