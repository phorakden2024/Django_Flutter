from django.contrib import admin 
from django.urls import include, path
from swagger import schema_view
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, LoginView 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# Configure Swagger Schema


urlpatterns = [
        # Auth
        path("register/", RegisterView.as_view(), name="register"),
        path("login/", LoginView.as_view(), name="login"),
        # Product URLs
        path('', include("api_services.api_urls.product_urls")),
        # Category URLs
        path('', include("api_services.api_urls.category_urls")),
        ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)