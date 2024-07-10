from django.urls import path

from task.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDoneView

urlpatterns = [
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/done/", TaskDoneView.as_view(), name="task-done"),
    ]

app_name = "task"
