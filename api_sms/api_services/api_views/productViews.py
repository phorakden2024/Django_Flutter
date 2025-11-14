import os
from django.http import HttpResponse, JsonResponse
from api_services.serialazer.ProductSerializer import ProductSerializer
from rest_framework import status,viewsets# type: ignore 
from rest_framework.decorators import api_view  # type: ignore 
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore 
from rest_framework.response import Response # type: ignore
from api_services.models import Product
from django.db.models import Q


@swagger_auto_schema(method='get', operation_summary="Get all products", responses={200: openapi.Response(description="List of all products")})
@api_view(['GET'])
def product_show(request):
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@swagger_auto_schema(method='get', operation_summary="Show a product by id")
@api_view(['GET'])
def show_product_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
name = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the product", type=openapi.TYPE_STRING)
@swagger_auto_schema(method='get', operation_summary="Search products by name",manual_parameters=[name], responses={200: ProductSerializer(many=True)})
@api_view(['GET'])
def search_by_name(request):
    try:
        name = request.query_params.get('name', None)
        if name is not None:
           products = Product.objects.filter(
               Q(name__icontains=name)
           )
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@swagger_auto_schema(method='post', operation_summary="Create a porduct",consumes=['multipart/form-data'],request_body=ProductSerializer)
@api_view(['POST'])
def create_product(request):
   product = Product()
   product.name = request.data['name']
   product.description = request.data['description']
   product.category_id_id = request.data['category_id']
   product.image = request.data['image']
   if product.image!="None" and product.image!="":    
        data ={
            'name': product.name,
            'description': product.description,
            'category_id': product.category_id_id,
            'image': product.image
            }
   else:
       data ={
            'name': product.name,
            'description': product.description,
            'category_id': product.category_id_id,
       }
   serializer = ProductSerializer(data=data)
   if serializer.is_valid():
       serializer.save()
       return JsonResponse({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
   else:
       return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
@swagger_auto_schema(method='put', operation_summary="Update a product by id",request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['name', 'description', 'category_id'],
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the product'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the product'),
        'category_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the category')
    }
))
@api_view(['PUT'])
def update_product(request, id):
    try:
        product = Product.objects.get(id=id)
        if 'name' in request.data:
            product.name = request.data['name']
        if 'description' in request.data:
            product.description = request.data['description']
        if 'category_id' in request.data:
            product.category_id_id = request.data['category_id']
        if 'image' in request.data:
            image_path = product.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            product.image = request.data['image']
        product.save()
        return JsonResponse({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
@swagger_auto_schema(method='delete', operation_summary="Delete a product by id")
@api_view(['DELETE'])
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        image_path = product.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
