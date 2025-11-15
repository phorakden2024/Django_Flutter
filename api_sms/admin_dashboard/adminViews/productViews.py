from django.shortcuts import render ,redirect
from api_services.models import Product,Category
from ..models import *
import datetime
import sweetify


def product(request):
          products = Product.objects.all()
          return render(request, 'setting/products/index.html', {'products': products})
def addform(request):
          category = Category.objects.all()
          return render(request, 'setting/products/create.html', {'categories': category})
def store(request):
          if request.method == 'POST':
                    product = Product()
                    product.name = request.POST['product_name']
                    product.description = request.POST['product_desc']
                    product.category_id_id = request.POST['cate_id']
                    if len(request.FILES) > 0:          
                        product.image = request.FILES['product_image']
                    if request.POST['is_active'] == 'true':
                        product.is_active = True
                    else:
                        product.is_active = False
                    product.save()
                    sweetify.success(request, 'Product created successfully')
                    return redirect('/product/')
          return render(request, 'setting/products/index.html')
def edit(request, id):
          product = Product.objects.get(id=id)
          category = Category.objects.all()
          return render(request, 'setting/products/edit.html', {'products': product, 'categories': category})
def update(request, id):
          if request.method == 'POST':            
                    product = Product.objects.get(id=id)
                    product.name = request.POST['product_name']
                    product.description = request.POST['product_desc']
                    product.category_id_id = request.POST['cate_id']
                    if len(request.FILES) > 0:
                        if product.image:
                            product.image.delete()     
                        product.image = request.FILES['product_image']
                    product.save()
                    sweetify.success(request, 'Product updated successfully')
                    return redirect('/product/')
          return render(request, 'setting/products/index.html')
def delete(request, id):
          product = Product.objects.get(id=id)
          if product.image:
              product.image.delete()
          product.delete()
          sweetify.success(request, 'Product deleted successfully')
          return redirect('/product/')