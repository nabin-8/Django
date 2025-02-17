from django.urls import path
from .views import TodoListView, TaskCreate, TaskUpdate, TaskDelete, RegisterView

urlpatterns = [
    path('', TodoListView.as_view(), name='todoList'),
    path('create/', TaskCreate.as_view(), name='create_task'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='edit_task'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
]