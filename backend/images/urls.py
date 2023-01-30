from images import views
from django.urls import include, path


urlpatterns = [
    path('',views.Images.as_view()),
    path('/tasks/<str:task_id>',views.get_task)
]
