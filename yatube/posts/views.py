from django.shortcuts import render, get_object_or_404

from .models import Post, Group


elements_on_page = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:elements_on_page]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:elements_on_page]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
