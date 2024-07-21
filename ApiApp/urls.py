from django.urls import path
from ApiApp.views import *

urlpatterns = [
    path("", List_tasks, name="list_tasks"),
    path("task/", Create_tasks, name="create_task"),
    path("task/<int:id>/", Task, name="task_detail"),
    path("task/delete/<int:id>/", Delete_task, name="delete_task"),
    path("task/update/<int:id>/", Update_task, name="update_task")
]
