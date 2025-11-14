from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sweetify
# Create your views here.

@login_required(login_url='/login/')
def admin_dashboard(request):
    return render(request, 'index.html')
def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user :
            if user.is_superuser:
                login(request, user)
                sweetify.success(request, 'Welcome Admin Dashboard' + user_name,  persistent='OK')
                return redirect("/",context={'user':user})
            else:
                sweetify.error(request, 'Access Denied',  persistent='OK')
                return redirect("/login/")
    return render(request, 'Auth/login.html')
def log_out(request):
    logout(request)
    return redirect('/')
        