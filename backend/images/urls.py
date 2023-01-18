from images import views
from django.urls import include, path


urlpatterns = [
    path('',views.Images.as_view()),
]
