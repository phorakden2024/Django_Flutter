from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from my_app.models import Student
from my_app.my_serializer.student_serializer import StudentSerializer
from rest_framework import status # type: ignore 
from rest_framework.decorators import api_view  # type: ignore 
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore
from django.db.models import Q

@api_view(['GET'])
def student_show(request):
    try:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def paginated_students(request):
    try:
        students = Student.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of students per page
        paginated_students = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(paginated_students, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@swagger_auto_schema(method='post', request_body=StudentSerializer)
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Student created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=StudentSerializer)
@api_view(['PUT'])
def student_update(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def student_search_by_id(request, id):
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)


name = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the student", type=openapi.TYPE_STRING)
@swagger_auto_schema(method='get', manual_parameters=[name], responses={200: StudentSerializer(many=True)})
@api_view(['GET'])
def student_search_by_name(request):
    name = request.query_params.get('name', None)
    if name is not None:
        students = Student.objects.filter(
            Q(first_name__icontains=name) |
            Q(last_name__icontains=name)
        )
        if students.exists():
            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', manual_parameters=[name], responses={200: StudentSerializer(many=True)})
@api_view(['GET'])
def student_search_by_name_with_pagination(request):
    name = request.query_params.get('name', None)
    if name is not None:
        students = Student.objects.filter(
            Q(first_name__icontains=name) |
            Q(last_name__icontains=name)
        )
        if students.exists():
            paginator = PageNumberPagination()
            paginator.page_size = 2  # Number of students per page
            paginated_students = paginator.paginate_queryset(students, request)
            serializer = StudentSerializer(paginated_students, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return JsonResponse({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
