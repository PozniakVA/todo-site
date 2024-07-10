from django.urls import path

from task.views import TaskListView, TaskCreateView

urlpatterns = [
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "task"
