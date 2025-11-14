from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore 
from rest_framework.response import Response # type: ignore
from api_services.models import Category
from rest_framework import status # type: ignore 
from rest_framework.decorators import api_view  # type: ignore
from api_services.serialazer.CategorySerializer import CategorySerializer
from django.db.models import Q

@swagger_auto_schema(method='get',operation_summary="Show all categories", responses={200: openapi.Response(description="List of all categories")},
)
@api_view(['GET'])
def category_show(request):
    try:
        categories = Category.objects.all()
        if not categories.exists():
            return JsonResponse({'message': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@swagger_auto_schema(method='get',operation_summary="Show a category by id", responses={200: openapi.Response(description="Category details")})
@api_view(['GET'])
def show_category_by_id(request, id):
    try:
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
name = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the category", type=openapi.TYPE_STRING)
@swagger_auto_schema(method='get',operation_summary="Search categories by name",manual_parameters=[name], responses={200: CategorySerializer(many=True)})
@api_view(['GET'])
def category_search_by_name(request):
    try:
        name = request.query_params.get('name', None)
        if name is not None:
           categorys = Category.objects.filter(
               Q(name__icontains=name)
           )
        else:
            categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@swagger_auto_schema(method='post',operation_summary="Create a category", request_body=openapi.Schema(
          type=openapi.TYPE_OBJECT,
          required=['name', 'description'],
          properties={
                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the category'),
                    'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the category')
          }
))
@api_view(['POST'])
def create_category(request):
    data = request.data
    category = Category(name=data['name'], description=data['description'])
    category.save()
    return JsonResponse({'message': 'Category created successfully'}, status=status.HTTP_201_CREATED)
@swagger_auto_schema(method='put',operation_summary="Update a category by id", request_body=openapi.Schema(
          type=openapi.TYPE_OBJECT,
          required=['name'],
          properties={
                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the category'),
                    'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the category')
          }
))
@api_view(['PUT'])
def update_category(request, id):
    try:
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Category edited successfully'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@swagger_auto_schema(method='delete',operation_summary="Delete a category by id",)
@api_view(['DELETE'])
def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse({'message': 'Category deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
