from django.urls import reverse_lazy
from django.views import generic

from tag.forms import TagForm
from tag.models import Tag


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tag:tag-list")
