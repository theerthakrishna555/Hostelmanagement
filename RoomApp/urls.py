from django.urls import path
from RoomApp import views

urlpatterns = [
    path('Add_room/',views.Add_room,name='Add_room'),
    path('update_room/<int:room_id>/',views.update_room,name='update_room'),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),


]