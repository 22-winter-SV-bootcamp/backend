from images import views
from django.urls import include, path

urlpatterns = [
        path('',views.get_ai_result),
]
