from django.contrib import admin 
from django.urls import include, path
from swagger import schema_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("admin_dashboard.admin_urls")),
    path('', include("api_services.api_main_urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('', include("my_app.my_app_urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


