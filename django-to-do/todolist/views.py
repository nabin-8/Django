from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.utils import timezone


# Task List View
class TodoListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_tasks = Task.objects.filter(user=self.request.user)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['incomplete_tasks_count'] = user_tasks.filter(complete=False).count()  # Count incomplete tasks
        context['now'] = timezone.now()
        return context

# Task Create View
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todoList/task_create.html'
    success_url = reverse_lazy('todoList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super(TaskCreate, self).form_valid(form)

# Task Update View
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todoList/task_update.html'
    success_url = reverse_lazy('todoList')
    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super(TaskUpdate, self).form_valid(form)

# Task Delete View
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'todoList/task_delete.html'
    success_url = reverse_lazy('todoList')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if response.status_code == 302:
            messages.success(self.request, 'Task deleted successfully!')
        return response

# User Registration View
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'todoList/register.html'
    success_url = reverse_lazy('todoList')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Log the user in after successful registration
        from django.contrib.auth import login
        login(self.request, self.object)
        messages.success(self.request, 'Registration successful! Welcome!')
        return response


# Login View
class CustomLoginView(LoginView):
    template_name = 'todoList/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'You have logged in successfully!')
        return reverse_lazy('todoList')
