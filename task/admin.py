from django.contrib import admin

from task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content",)
    search_fields = ("name",)
