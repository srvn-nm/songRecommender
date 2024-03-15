from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/music/', include('service_one.urls')),
    path('api/recognize/', include('service_two.urls')),
    path('api/recommendations/', include('service_three.urls')),
]