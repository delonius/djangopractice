from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:blog_id>/", views.blog_view, name="entry"),
    path("author/<str:author>", views.filter_author, name="author"),
    path("tag/<str:tag>", views.filter_tag, name="tag"),
]