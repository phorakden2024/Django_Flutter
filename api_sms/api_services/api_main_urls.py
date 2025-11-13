from django.contrib import admin 
from django.urls import include, path
from swagger import schema_view
from django.conf import settings
from django.conf.urls.static import static
from api_services import views  

urlpatterns = [
        # path('', views.index, name='home'),
        path('', include("api_services.api_urls.product_urls")),
        path('', include("api_services.api_urls.category_urls")),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)