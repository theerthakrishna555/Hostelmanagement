from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('add_hostel/',views.add_hostel,name='add_hostel'),
    path('view_hostel/',views.view_hostel_page,name='view_hostel'),
    path('admin_hostel_page/',views.admin_hostel_page,name='admin_hostel_page'),
    path('approve/<int:hostel_id>/', views.approve_hostel, name='approve'),
    path('Edit_hostel/<int:hostel_id>/',views.Edit_hostel,name='Edit_hostel'),

    path('Room_page',views.Room_page,name='Room_page'),
    path('View_Room',views.View_Room,name='View_Room'),
    path('Edit_room/<int:room_id>/',views.Edit_room,name='Edit_room'),

]