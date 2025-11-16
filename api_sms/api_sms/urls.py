from django.contrib import admin 
from django.urls import include, path,re_path
from swagger import schema_view
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
   openapi.Info(
      title="Django API",
      default_version='v1',
      description="API documentation for Register and Login endpoints",
      # Add contact, license info if needed
   ),
   public=True,
   permission_classes=(AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Admin
    path('', include("admin_dashboard.admin_urls")),
    
    # API
    path('api/', include("api_services.api_main_urls")),
    # path('', include("my_app.my_app_urls")),
    
    # Swagger Docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


