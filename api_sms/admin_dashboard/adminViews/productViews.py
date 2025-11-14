from django.shortcuts import render ,redirect
from api_services.models import Product
from ..models import *
import datetime
import sweetify


def product(request):
          return render(request, 'setting/products/index.html')
def product_list(request):
          products = Product.objects.all()
          return render(request, 'product_list.html', {'products': products})