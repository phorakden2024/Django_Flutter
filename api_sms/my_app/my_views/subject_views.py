from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from my_app.models import Subject
from my_app.my_serializer.subject_serializer import SubjectSerializer
from rest_framework import status # type: ignore 
from rest_framework.decorators import api_view  # type: ignore 
from drf_yasg.utils import swagger_auto_schema # type: ignore 
from drf_yasg import openapi # type: ignore 
from rest_framework.pagination import PageNumberPagination  # type: ignore

@api_view(['GET'])
def paginated_subjects(request):
    try:
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of subjects per page
        subjects = Subject.objects.all()
        paginated_subjects = paginator.paginate_queryset(subjects, request)
        serializer = SubjectSerializer(paginated_subjects, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def find_by_id(request, id):
    try:
        subject = Subject.objects.get(id=id)
        if(subject is None):
            return JsonResponse({'message': f'Subject not found with id:{id}'})
        serializer = SubjectSerializer(subject)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)

#search by name
name = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the subject", type=openapi.TYPE_STRING)
@swagger_auto_schema(method='get', manual_parameters=[name], responses={200: SubjectSerializer(many=True)})
@api_view(['GET'])
def subject_search_by_name(request):
    try:
        name = request.query_params.get('name', None)
        if name is not None:
            subjects = Subject.objects.filter(subject_name__icontains=name)
        else:
            # subjects = Subject.objects.all()
            return JsonResponse({'message': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#search by name with pagination
name = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the subject", type=openapi.TYPE_STRING)
@swagger_auto_schema(method='get', manual_parameters=[name], responses={200: SubjectSerializer(many=True)})
@api_view(['GET'])
def subject_search_by_name_with_pagination(request):
    try:
        name = request.query_params.get('name', None)
        if not name:
            return JsonResponse({'message': '"name" parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of subjects per page
        subjects = Subject.objects.filter(subject_name__icontains=name)
        if (subjects.count() == 0):
            return JsonResponse({'message': 'No subjects found matching the name'}, status=status.HTTP_404_NOT_FOUND)
        paginated_subjects = paginator.paginate_queryset(subjects, request)
        serializer = SubjectSerializer(paginated_subjects, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(method='get', responses={200: SubjectSerializer(many=True)})
@api_view(['GET'])
def subject_show(request):
   try:
       subjects = Subject.objects.all()
       serializer = SubjectSerializer(subjects, many=True)
       return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
   except Exception as e:
       return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@swagger_auto_schema(method='post', request_body=SubjectSerializer)
@api_view(['POST'])
def create_subject(request):
    try:
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Subject created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@swagger_auto_schema(method='put', request_body=SubjectSerializer)
@api_view(['PUT'])
def update_subject(request,id):
    subject_existing = Subject.objects.filter(id=id).first()
    if(subject_existing is None):
        return JsonResponse({'message': f'Subject not found with id:{id}'})
    subject_existing.subject_name = request.data['subject_name']
    data = {
        'subject_name': subject_existing.subject_name
    }
    serializer = SubjectSerializer(subject_existing, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Subject updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_subject(request, id):
    subject_existing = Subject.objects.filter(id=id).first()
    if subject_existing is None:
        return JsonResponse({'message': f'Subject not found with id:{id}'}, status=status.HTTP_404_NOT_FOUND)
    subject_existing.delete()
    return JsonResponse({'message': f'Subject deleted successfully'}, status=status.HTTP_200_OK)
