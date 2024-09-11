# myapp/urls.py

# myapp/urls.py

from django.urls import path
from .views import register_view, login_view, task_list, add_task, edit_task, delete_task

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('tasks/', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]

