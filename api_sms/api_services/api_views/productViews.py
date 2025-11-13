from django.http import HttpResponse,JsonResponse
from rest_framework import status # type: ignore 
from rest_framework.decorators import api_view  # type: ignore 
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore 
from rest_framework.response import Response # type: ignore

@api_view(['GET'])
def create_product(request):
          return JsonResponse("Hello, world. You're at the my_app index.")