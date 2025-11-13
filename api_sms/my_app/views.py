from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view # type: ignore
# Create your views here.

@api_view(['GET']) 
def index(request):
    return HttpResponse("Hello, world. You're at the my_app index.")

# @api_view(['GET'])
# def find_id(request, id):
#     return HttpResponse(f"You're looking for item {id}.")
