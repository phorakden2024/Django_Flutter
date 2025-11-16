from django.contrib import admin 
from django.urls import include, path
from api_services import views
from api_services.api_views import categoryViews
from swagger import schema_view

urlpatterns = [
          path('categories', categoryViews.category_show),
          path('categories/', categoryViews.create_category),
          path('categories/<int:id>/', categoryViews.update_category),
          path('categories/<int:id>/delete/', categoryViews.delete_category),
          path('categories/<int:id>/show_by_id/', categoryViews.show_category_by_id),
          path('categories/search_by_name/', categoryViews.category_search_by_name),
]