from django.shortcuts import render ,redirect
from api_services.models import Product
from ..models import *
import datetime
import sweetify


def unit_of_measurement(request):
          return render(request,'setting/uom/index.html')