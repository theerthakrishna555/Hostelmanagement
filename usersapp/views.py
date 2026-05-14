from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from usersapp.forms import UserRegistration
from  django.urls import reverse_lazy

# Create your views here.

class login_view(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def register_page(request):
    return render(request,'registration/register.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.save()
            return redirect('login')


    return  render(request,'registration/register.html')

class admin_login(LoginView):
    template_name = 'registration/admin_login.html'

    def form_valid(self,form):
        user = form.get_user()

        if user.role != 'admin' and not user.is_superuser:
            form.add_error(None,'you are not authorized as admin')
            return  self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


def warden_reg(request):
    return render(request,'registration/warden_register.html')

def register_warden(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'warden'
            user.save()
            return redirect('warden_login')
        else:
            print(form.errors)
    else:
        form = UserRegistration()

    return render(request, 'registration/warden_register.html')

class login_warden(LoginView):
    template_name = 'registration/warden_login.html'

    def get_success_url(self):
        user = self.request.user

        if user.role == 'warden':
            return reverse_lazy('dashboard')
        else:
            return reverse_lazy('warden_login')






