from django.urls import path
from . import views, api

app_name='cars'

urlpatterns = [

    # Cars Home
    path('', views.car_home, name='cars-home'),

    # View all cars
    path('cars-list', views.car_list, name='car-list'),

    # View a car detail
    path('car-list/<int:id>', views.car_detail, name='car-details'),
    
    # add car
    path('add',views.add_car, name='add-car'),

    # change
    path('update-car/<int:id>', views.car_update, name='update-car'),

    # # delete an car
    path('delete-car/<int:pk>', views.car_delete, name='delete-car'),
    
    # customer cars
    path('customer-cars/<str:pk>', views.customerCarsPage, name='customer-cars'),

    ########################### APIs urls ###########################
    # get cars total number
    path('api/count', api.cars_count_view, name='count-cars'),
    
    # get a floor cars number
    path('api/count-floor-cars/<int:id>', api.floor_cars_count_view, name='count-floor-cars'),
    
    # get cost of car
    path('api/car-cost/<int:id>', api.calulate_car_cost, name='car-cost'),

]