from django.contrib import admin 
from django.urls import include, path
from api_services import views
from api_services.api_views import categoryViews
from swagger import schema_view

urlpatterns = [
          path('api/v1/categories', categoryViews.category_show),
          path('api/v1/categories/', categoryViews.create_category),
          path('api/v1/categories/<int:id>/', categoryViews.update_category),
          path('api/v1/categories/<int:id>/delete/', categoryViews.delete_category),
]