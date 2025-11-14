from django.shortcuts import render ,redirect
from api_services.models import Category
from ..models import *
import datetime
import sweetify


def category(request):
          return render(request, 'setting/category/index.html')