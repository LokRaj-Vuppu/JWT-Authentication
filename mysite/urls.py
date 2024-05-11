from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest_api/", include("rest_apis.urls")),
]
