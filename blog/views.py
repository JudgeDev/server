"""Blog views"""
from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Comment, Post


def blog_index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_on")  # query all posts
    context: Dict[str, str] = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    # get comments from a form
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context: Dict[str, str] = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)


def blog_category(request: HttpRequest, category: str) -> HttpResponse:
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)
