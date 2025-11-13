from django.contrib import admin 
from django.urls import include, path
from my_app import views
from my_app.my_views import subject_views 
from my_app.my_views import teacher_views
from my_app.my_views import student_views
from swagger import schema_view
urlpatterns = [
    path('', views.index, name='home'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   
    
    #Subject Route
    path('api/v1/subjects', subject_views.create_subject),
    path('api/v1/subjects/', subject_views.subject_show),
    path('api/v1/subjects/<int:id>', subject_views.delete_subject),
    path('api/v1/subjects/<int:id>/', subject_views.update_subject),
    path('api/v1/subjects/paginated/', subject_views.paginated_subjects),
    path('api/v1/subjects/search_by_name/', subject_views.subject_search_by_name),
    path('api/v1/subjects/find_by_id/<int:id>/', subject_views.find_by_id),
    path('api/v1/subjects/search_by_name_paginated/', subject_views.subject_search_by_name_with_pagination),
    
    #Teacher Route
    path('api/v1/teachers', teacher_views.create_teacher),
    path('api/v1/teachers/', teacher_views.teacher_show),
    path('api/v1/teachers/<int:id>', teacher_views.delete_teacher),
    path('api/v1/teachers/<int:id>/', teacher_views.update_teacher),
    path('api/v1/teachers/paginated/', teacher_views.paginated_teachers),
    path('api/v1/teachers/search_by_name/', teacher_views.teacher_search_by_name),
    path('api/v1/teachers/find_by_id/<int:id>/', teacher_views.find_teacher_by_id),
    path('api/v1/teachers/search_by_name_paginated/', teacher_views.search_by_name_with_pagination),

    #Student Route
    path('api/v1/students', student_views.student_create),
    path('api/v1/students/', student_views.student_show),
    path('api/v1/students/<int:id>', student_views.student_delete),
    path('api/v1/students/<int:id>/', student_views.student_update),
    path('api/v1/students/paginated/', student_views.paginated_students),
    path('api/v1/students/search_by_name/', student_views.student_search_by_name),
    path('api/v1/students/find_by_id/<int:id>/', student_views.student_search_by_id),
    path('api/v1/students/search_by_name_paginated/', student_views.student_search_by_name_with_pagination),

]

