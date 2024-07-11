from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class TaskDoneView(generic.View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.done = not task.done
        task.save()
        return HttpResponseRedirect(reverse_lazy("task:task-list"))
