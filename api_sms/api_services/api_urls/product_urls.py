from django.contrib import admin 
from django.urls import include, path
from api_services import views
from swagger import schema_view
from api_services.api_views import productViews


urlpatterns = [
          path('api/v1/products', productViews.product_show),
          path('api/v1/products/', productViews.create_product),
          path('api/v1/products/<int:id>/', productViews.update_product),
          path('api/v1/products/<int:id>/delete/', productViews.delete_product),
          path('api/v1/products/<int:id>/show_by_id/', productViews.show_product_by_id),
          path('api/v1/products/search_by_name/', productViews.search_by_name),
]