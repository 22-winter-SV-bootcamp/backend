from .views import *
from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('',views.ShowStyleView.as_view())
]
