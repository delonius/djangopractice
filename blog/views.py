from django.shortcuts import render
from .models import Blog


def get_blogs_tags():
    blogs = Blog.objects.all()
    tags = {blog.id: blog.tags.split(', ') for blog in blogs}
    return blogs, tags


def index(request):
    blogs, tags = get_blogs_tags()
    return render(request, "blog/index.html", {
        "blogs": blogs,
        "tags": tags,
    })


def blog_view(request, blog_id):
    blog = Blog.objects.get(pk=int(blog_id))
    return render(request, "blog/blog.html", {
        "blog": blog,
    })


def filter_author(request, author):
    blogs, tags = get_blogs_tags()
    blogs = Blog.objects.filter(author=author)
    return render(request, "blog/index.html", {
        "blogs": blogs,
        "tags": tags,
        "filter_type": "author",
        "author": author,
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
    })
