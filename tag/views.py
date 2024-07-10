from django.views import generic

from tag.models import Tag


class TagListView(generic.ListView):
    model = Tag
