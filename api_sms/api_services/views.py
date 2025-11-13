from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view # type: ignore
# Create your views here.

@api_view(['GET']) 
def index(request):
    return HttpResponse("Hello, world. You're at the api services index.")