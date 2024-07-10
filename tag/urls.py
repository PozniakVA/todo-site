from django.urls import path

from tag.views import TagListView, TagCreateView, TagUpdateView

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagUpdateView.as_view(), name="tag-delete"),
]

app_name = "tag"
