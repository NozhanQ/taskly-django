from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import task_list
from . import views

urlpatterns = [
    path("", task_list, name="task_list"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
