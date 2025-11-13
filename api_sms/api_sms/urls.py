from django.contrib import admin 
from django.urls import include, path
from swagger import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("my_app.my_app_urls")),
    path('', include("api_services.api_urls.product_urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]


