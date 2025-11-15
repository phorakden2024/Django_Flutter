from django.shortcuts import render ,redirect
from api_services.models import Category
from ..models import *
import datetime
import sweetify


def category(request):
    category = Category.objects.all()
    return render(request, 'setting/category/index.html', {'categories': category})

def addform(request):
    return render(request, 'setting/category/create.html')

def store(request):
    name = request.POST['name']
    description = request.POST['description']
    is_active = request.POST.get('is_active', False)
    if is_active == 'false':
        is_active = False
    elif is_active == 'true':
        is_active = True
    else:
        raise ValueError('["false" value must be either True or False.')
    category = Category(name=name, description=description, is_active=is_active)
    category.save()
    sweetify.success(request, 'Category created successfully')
    return redirect('/category/')
def edit(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'setting/category/edit.html', {'categories': category})

def update(request, id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        category.name = request.POST['name']
        category.description = request.POST['description']
        is_active = request.POST.get('is_active', False)    
        if is_active == 'false':
            is_active = False
        elif is_active == 'true':
            is_active = True
        else:
            raise ValueError('["false" value must be either True or False.')
        category.is_active = is_active
        category.save()
        sweetify.success(request, 'Category updated successfully')
        return redirect('/category/')
    return render(request, 'setting/category/edit.html')

def delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    sweetify.success(request, 'Category deleted successfully')
    return redirect('/category/')