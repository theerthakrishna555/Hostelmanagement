from django.urls import path
from hostelapp import views

urlpatterns = [
    path('add_hostel_details/',views.add_hostel_details,name='add_hostel_details'),
    path('update_hostel/<int:hostel_id>',views.update_hostel,name='update_hostel'),
    path('delete_hostel/<int:hostel_id>',views.delete_hostel,name='delete_hostel'),
]