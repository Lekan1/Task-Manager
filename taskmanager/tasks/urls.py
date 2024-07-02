from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, index, create_task, update_task, delete_task,update_task_status

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create_task'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('update_task_status/', update_task_status, name='update_task_status'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
