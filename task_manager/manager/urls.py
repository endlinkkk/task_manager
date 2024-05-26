from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoView.as_view(), name="todo"),
    path("completed_tasks", views.get_completed_tasks, name="completed_tasks"),
]
