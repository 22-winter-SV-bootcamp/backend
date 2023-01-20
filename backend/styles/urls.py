from .views import *
from . import views
from django.urls import include, path


urlpatterns = [
    path('',views.ShowStyleView.as_view())
]
