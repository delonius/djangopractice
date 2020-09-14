from django.shortcuts import render
from .models import Blog
from django.apps import apps
Task = apps.get_model('tasks', 'Task')


def tasks_due(request):
    return len(Task.objects.filter(user=request.user).all()) if request.user.is_authenticated else None


def get_blogs_tags():
    blogs = Blog.objects.all()
    tags = {blog.id: blog.tags.split(', ') for blog in blogs}
    return blogs, tags


def index(request):
    blogs, tags = get_blogs_tags()
    return render(request, "blog/index.html", {
        "blogs": blogs,
        "tags": tags,
        "tasks_due": tasks_due(request),
    })


def blog_view(request, blog_id):
    blog = Blog.objects.get(pk=int(blog_id))
    return render(request, "blog/blog.html", {
        "blog": blog,
        "tasks_due": tasks_due(request),
    })


def filter_author(request, author):
    blogs, tags = get_blogs_tags()
    blogs = Blog.objects.filter(author=author)
    return render(request, "blog/index.html", {
        "blogs": blogs,
        "tags": tags,
        "filter_type": "author",
        "author": author,
        "tasks_due": tasks_due(request),
    })


def filter_tag(request, tag):
    blogs, tags = get_blogs_tags()
    filtered_blogs = []
    for blog in blogs:
        if tag in str(blog.tags):
            filtered_blogs.append(blog)
    return render(request, "blog/index.html", {
        "blogs": filtered_blogs,
        "tags": tags,
        "filter_type": "tag",
        "tag": tag,
        "tasks_due": tasks_due(request),
    })
