from django.urls import path
from . import views

urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    # path("completeTask/<int:task_id>/", views.completeTask, name="completeTask"),
]
