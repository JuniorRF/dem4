from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post, Group, Comment
from .forms import PostForm, CommentForm


User = get_user_model()


def index(request):
    posts = Post.objects.all()[:settings.SHOW_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:settings.SHOW_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    post_list = profile.posts.all().select_related(
        'group', 'author')
    context = {'post_list': post_list}
    return render(request, 'posts/profile.html', context)


@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', request.user)
    return render(request, 'posts/new_post.html', context)


def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    context = {'post': post, 'comments':comments, 'form': form}
    return render(request, 'posts/detail.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None, instance=post)
    context = {'form':form}
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('posts:detail', pk=post.pk)
    return render(request, 'posts/new_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(dir(request))
    if post.author == request.user:
        post.delete()
    return redirect('posts:homepage')


def add_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=pk)
        comment.author = request.user
        comment.save()
    return redirect('posts:detail', pk)


def del_comment(request, pk, id_comment):
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, id=id_comment)
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:detail', pk=post.pk)