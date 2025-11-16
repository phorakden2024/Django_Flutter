import os
from django.http import HttpResponse, JsonResponse
from api_services.serialazer.ProductSerializer import ProductSerializer
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore 
from rest_framework.response import Response # type: ignore
from rest_framework import status,viewsets# type: ignore 
from rest_framework.decorators import api_view  # type: ignore 
from rest_framework import generics
from api_services.models import Product
from django.db.models import Q


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



