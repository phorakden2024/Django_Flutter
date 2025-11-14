from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from admin_dashboard.adminViews import productViews,categoryViews,uomViews


urlpatterns = [
    path('', views.admin_dashboard, name='dashboard_home'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    
    #product
    path('product/', productViews.product, name='product'),
    
    
    #category
    path('category/', categoryViews.category, name='category'),
    #unit of measurement
    path('unit/', uomViews.unit_of_measurement, name='unit'),
    
] 


