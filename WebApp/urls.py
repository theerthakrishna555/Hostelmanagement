from django.urls import path
from WebApp.views import *


urlpatterns = [
    path('',home_page,name='home'),
    path('home/',home_page,name='home'),
    path('hostel_list_page/',hostel_list_page,name='hostel_list_page'),
    path('search-hostel/', search_hostel, name='search_hostel'),
    path('Room_list_page/<int:filtered_hostel_id>/',Room_list_page,name='Room_list_page'),
    path('single_room_page/<int:room_id>/',single_room_page,name='single_room_page'),

    path('booking/<int:room_id>/', booking_page, name='booking_page'),
    path('payment_page/<int:id>/', payment_page, name='payment_page'),
    path('succes_page/<int:id>/',succes_page,name='succes_page'),


    path('About_page/',About_page,name='About_page'),
    path('contact_page/',contact_page,name='contact_page'),
    path('all_rooms_page/',all_rooms_page,name='all_rooms_page'),
]