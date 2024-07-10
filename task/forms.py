from django import forms
from django.core.checks import Tags
from django.forms import CheckboxSelectMultiple

from tag.models import Tag
from task.models import Task


class TaskForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    deadline = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "tags"
        )
