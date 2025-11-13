from django.contrib import admin 
from django.urls import include, path
from api_services import views
from api_services.api_views import productViews
from swagger import schema_view

urlpatterns = [
          path('', views.index, name='home'),
          path('api/v1/products', productViews.create_product),
]