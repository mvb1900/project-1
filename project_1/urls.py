from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app_api_gateway.urls"), name="app_api_gateway"),
]
