from django.db import models

from tag.models import Tag


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
    )

    class Meta:
        ordering = ("done", "-datetime",)

    def __str__(self) -> str:
        return self.content
