from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from admin_dashboard.adminViews import productViews,categoryViews,uomViews,userViews


urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('', views.admin_dashboard, name='dashboard_home'),
    #product
    path('product/', productViews.product, name='product'),
    path('product/addform/', productViews.addform, name='addform_product'),
    path('product/store/', productViews.store, name='store_product'),
    path('product/edit/<int:id>/', productViews.edit, name='edit_product'),
    path('product/update/<int:id>/', productViews.update, name='update_product'),
    path('product/delete/<int:id>/', productViews.delete, name='delete_product'),
    
    
    #category
    path('category/', categoryViews.category, name='category'),
    path('category/addform/', categoryViews.addform, name='addform_category'),
    path('category/store/', categoryViews.store, name='store_category'),
    path('category/edit/<int:id>/', categoryViews.edit, name='edit_category'),
    path('category/update/<int:id>/', categoryViews.update, name='update_category'),
    path('category/delete/<int:id>/', categoryViews.delete, name='delete_category'),
    
    #unit of measurement
    path('unit/', uomViews.unit_of_measurement, name='unit'),
    
    
    
    #User
    path('user/', userViews.user, name='user'),
    path('user/addform/', userViews.addform, name='addform_user'),
    path('user/store/', userViews.store, name='store_user'),
    path('user/edit/<int:id>/', userViews.edit, name='edit_user'),
    path('user/update/<int:id>/', userViews.update, name='update_user'),
    path('user/delete/<int:id>/', userViews.delete, name='delete_user'),
    path('user/view/<int:id>/', userViews.view, name='view_user'),
    
    #role
    # path('role/', views.role, name='role'),
    # path('role/addform/', views.addform, name='addform_role'),
    # path('role/store/', views.store, name='store_role'),
    # path('role/edit/<int:id>/', views.edit, name='edit_role'),
    # path('role/update/<int:id>/', views.update, name='update_role'),
    # path('role/delete/<int:id>/', views.delete, name='delete_role'),
] 


