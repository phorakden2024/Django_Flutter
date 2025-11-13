from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from my_app.models import Teacher
from my_app.my_serializer.teacher_serializer import TeacherSerializer
from rest_framework import status # type: ignore 
from rest_framework.decorators import api_view  # type: ignore 
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore
from django.db.models import Q


@api_view(['GET'])
def teacher_show(request):
    try:
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='post', request_body=TeacherSerializer)
@api_view(['POST'])
def create_teacher(request):
    try:
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Teacher created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 

@swagger_auto_schema(method='put', request_body=TeacherSerializer)
@api_view(['PUT'])
def update_teacher(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
        data = TeacherSerializer(teacher).data
        data.update(request.data)
        serializer = TeacherSerializer(teacher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Teacher updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Teacher.DoesNotExist:
        return JsonResponse({'message': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_teacher(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
        return JsonResponse({'message': 'Teacher deleted'}, status=status.HTTP_200_OK)
    except Teacher.DoesNotExist:
        return JsonResponse({'message': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#search by id
@api_view(['GET'])
def find_teacher_by_id(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Teacher.DoesNotExist:
        return JsonResponse({'message': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#search by name
name = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the teacher", type=openapi.TYPE_STRING)
@swagger_auto_schema(method='get', manual_parameters=[name], responses={200: TeacherSerializer(many=True)})
@api_view(['GET'])
def teacher_search_by_name(request):
    try:
        name = request.query_params.get('name', None)
        if name is not None:
            teachers = Teacher.objects.filter(
                Q(first_name__icontains=name) |
                Q(last_name__icontains=name) |
                Q(address__icontains=name)
            )
        else:
            teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#search by name with pagination
@swagger_auto_schema(method='get', manual_parameters=[name], responses={200: TeacherSerializer(many=True)})
@api_view(['GET'])
def search_by_name_with_pagination(request):
    try:
        name = request.query_params.get('name', None)
        if name is not None:
            teachers = Teacher.objects.filter(  
            	Q(first_name__icontains=name) |
                Q(last_name__icontains=name) |
                Q(address__icontains=name)
            )
        else:
            # teachers = Teacher.objects.all()
            return JsonResponse({'message': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of teachers per page
        paginated_teachers = paginator.paginate_queryset(teachers, request)
        serializer = TeacherSerializer(paginated_teachers, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def paginated_teachers(request):
    try:
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of teachers per page
        teachers = Teacher.objects.all()
        paginated_teachers = paginator.paginate_queryset(teachers, request)
        serializer = TeacherSerializer(paginated_teachers, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
