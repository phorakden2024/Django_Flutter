from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from ..models import *
import datetime
import sweetify

def user(request):
    user = User.objects.all()
    return render(request, 'setting/UserManagerment/user/index.html', {'users': user})
def addform(request):
    return render(request, 'setting/UserManagerment/user/create.html')
def store(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        is_superuser = request.POST.get('is_superuser') == 'on' if 'is_superuser' in request.POST else False
        is_active = request.POST.get('is_active') == 'on' if 'is_active' in request.POST else False
        is_staff = request.POST.get('is_staff') == 'on' if 'is_staff' in request.POST else False
        user = User.objects.create_user(
            username=username, 
            password=password, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            is_superuser=is_superuser, 
            is_active=is_active, 
            is_staff=is_staff)
        user.save()
        sweetify.success(request, 'User created successfully')
        return redirect('/user/')
def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'setting/UserManagerment/user/edit.html', {'user': user})
def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.is_superuser = request.POST.get('is_superuser') == 'on' if 'is_superuser' in request.POST else False
        user.is_active = request.POST.get('is_active') == 'on' if 'is_active' in request.POST else False
        user.is_staff = request.POST.get('is_staff') == 'on' if 'is_staff' in request.POST else False
        user.save()
        sweetify.success(request, 'User updated successfully')
        return redirect('/user/')
def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    sweetify.success(request, 'User deleted successfully')
    return redirect('/user/')
def view(request, id):
    user = User.objects.get(id=id)
    return render(request, 'setting/UserManagerment/user/edit.html', {'user': user , 'viewMode': viewMode})
