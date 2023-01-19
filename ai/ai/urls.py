
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/images',include('images.urls')),
    path('', include('django_prometheus.urls')),

]
