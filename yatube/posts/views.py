from django.shortcuts import render, get_object_or_404

from .models import Post, Group


ON_PAGE = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
