from django.contrib import admin 
from django.urls import include, path
from api_services import views
from swagger import schema_view
from api_services.api_views.productViews import  ProductView


urlpatterns = [
          path('products', ProductView.as_view(),),
          
          # path('products', productViews.product_show),
          # path('products/', productViews.create_product),
          # path('products/<int:id>/', productViews.update_product),
          # path('products/<int:id>/delete/', productViews.delete_product),
          # path('products/<int:id>/show_by_id/', productViews.show_product_by_id),
          # path('products/search_by_name/', productViews.search_by_name),
]