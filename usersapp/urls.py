from django.urls import path
from usersapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_page/',register_page,name='register_page'),
    path('register_save/',register,name='register_save'),
    path('admin_login/',admin_login.as_view(),name='admin_login'),
    path('warden_reg/',register_warden,name='warden_reg'),
    path('warden_login/',login_warden.as_view(),name='warden_login'),
]