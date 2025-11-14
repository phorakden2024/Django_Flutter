from django.contrib import admin 
from django.urls import include, path,re_path
from swagger import schema_view
from django.conf import settings
from django.conf.urls.static import static
from api_services import views 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# Configure Swagger Schema
schema_view = get_schema_view(
   openapi.Info(
      title="Django API",
      default_version='v1',
      description="API documentation for Register and Login endpoints",
      # Add contact, license info if needed
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
        
        path('', include("api_services.api_urls.product_urls")),
        path('', include("api_services.api_urls.category_urls")),
        path('', include("api_services.api_urls.UserAuth_urls")),
        # Swagger UI URLs
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)