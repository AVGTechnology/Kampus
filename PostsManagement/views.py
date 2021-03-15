from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import url
from requests import Response

from .forms import PostForm, CommentForm
from .models import *
from Userprofile.models import *
from django.contrib import messages


# Create your views here.


@login_required
def post(request):
    form = PostForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post was created Successfully!! .')
        messages.success(request, 'Create more posts!')
        return redirect('post')
    else:
        form = PostForm(user=request.user)
        messages.info(request, 'Creating Posting please wait...')

    return render(request, 'add_post.html', {"form": form, })


@login_required
def news_feed(request):
    posts = Post.objects.all().order_by('-timestamp')
    profile = UserProfile.objects.get(user=request.user)
    # postuser = posts, 'user'
    up = UserProfile.objects.all()
    comments = Comment.objects.all()[:2]
    context = {
        'up': up,
        'posts': posts,
        'profile': profile,
        'comments': comments,

    }
    return render(request, 'newsfeed.html', context)


@login_required
def like(request, pk):
    liked_post = get_object_or_404(Post, pk=pk)
    user = request.user

    if user in liked_post.like.all():
        liked_post.like.remove(user)
    else:
        liked_post.like.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def comment(request, pk):
    comments = request.GET.get('comment')
    com_post = Post.objects.get(pk=pk)

    form = CommentForm(request.POST)
    form.instance.comment = comments
    form.instance.post = com_post
    form.instance.user = request.user
    if form.is_valid():
        form.save()

    return redirect('comment_view', pk)


@login_required
def comment_view(request, pk):
    posts = Post.objects.get(pk=pk)
    comments = Comment.objects.all().filter(post=posts).order_by('timestamp')

    context = {

        'comments': comments,
        'posts': posts,
    }
    return render(request, 'comment_view.html', context)


def delete_post(request, pk):
    get_object_or_404(Post, pk=pk).delete()
    return redirect('user_profile')
