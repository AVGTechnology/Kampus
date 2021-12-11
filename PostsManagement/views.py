import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import url
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from urllib3.packages.six import BytesIO

from .forms import PostForm, CommentForm
from .models import *
from Userprofile.models import *
from django.contrib import messages
from fcm_django.models import FCMDevice

from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from moviepy.editor import *
from PIL import Image


class NewsFeed(ListView):
    model = Post
    paginate_by = 2
    context_object_name = 'posts'
    template_name = 'newsfeed.html'
    ordering = ['-timestamp']


class FullScreen(ListView):
    model = Post
    paginate_by = 1
    context_object_name = 'posts'
    template_name = 'fullscreen_view.html'
    ordering = ['-timestamp']


@login_required
def post(request):
    user_p = UserProfile.objects.get(user=request.user)
    follower = user_p.follower.all()
    form = PostForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        instance = form.save()
        messages.success(request, 'Post was created Successfully!! .')
        messages.success(request, 'Create more posts!')
        n_post = Post.objects.get(pk=instance.pk)
        caption = n_post.caption
        auth = n_post.user
        image = n_post.file
        device = FCMDevice.objects.all().filter(user__in=follower)
        device.send_message(title=f'{auth} created a new post on Kampus ', body=f'{caption} ',
                            icon='static/images/logo.png',
                            data={"Details": "Details"})
        return redirect('preview', n_post.pk)

    else:
        form = PostForm(user=request.user)
        messages.info(request, 'Creating Post, Uploading Video file take long time! please wait...')

    return render(request, 'add_post.html', {"form": form, })


@login_required
def preview(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'preview.html', {"posts": posts, })


import base64
import time
from django.core.files.base import ContentFile, File
from django.core.files.storage import FileSystemStorage


@login_required
def thumbnail(request, pk):
    destination_dir = os.path.join(settings.AWS_LOCATION, 'media', 'media', 'Post_thumbnail')
    # destination_dir = 'media', 'media', 'Post_thumbnail'
    os.makedirs(destination_dir, exist_ok=True)
    posts = Post.objects.get(pk=pk)
    # print(f"{posts.file.url}") print(posts.file.path) https://kampusstorage.fra1.digitaloceanspaces.com / media /
    # media / Post_Files / 1639068579411724267657957181444.j
    clip = VideoFileClip(f"{posts.file.url}")
    # clip = VideoFileClip(posts.file.path)
    # print(clip)
    # print(clip.reader.fps)
    # print(clip.duration)
    frame = clip.get_frame(2.00)
    # print(frame)
    # new_img_path = os.path.join(settings.DEFAULT_FILE_STORAGE, f"{posts.pk}.jpg")
    new_img_path = os.path.join(destination_dir, f"{posts.pk}.jpg")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_path)
    # file = open(os.path.join(settings.MEDIA_ROOT, 'media', 'Post_thumbnail', f"{posts.pk}.jpg"),'r')
    return redirect('index')


@login_required
def likes(request, pk):
    p_likes = get_object_or_404(Post, pk=pk)

    context = {
        'p_likes': p_likes,

    }
    return render(request, 'likes.html', context)


def full_screen(request):
    posts = Post.objects.all().order_by('-timestamp')[:1]
    context = {

        'posts': posts,

    }
    return render(request, 'fullscreen_view.html', context)


@csrf_exempt
@login_required
def like(request):
    pk = request.GET.get('pk', None)
    liked_post = get_object_or_404(Post, pk=pk)
    user = request.user
    # print(pk)
    if user in liked_post.like.all():
        liked_post.like.remove(user)
        unliked = 'unliked'
        data = {
            'unliked': unliked

        }

        return JsonResponse(data, status=200)
    else:
        liked_post.like.add(user)
        liked = 'liked'
        data = {
            'liked': liked

        }

        return JsonResponse(data, status=200)


@csrf_exempt
def comment_count(request):
    pk = request.GET.get('pk', None)
    cp = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all().filter(post=cp).count()
    print(comments)

    context = {
        'count': comments

    }

    return JsonResponse(context, status=200)


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


def comment_view(request, pk):
    posts = Post.objects.get(pk=pk)
    comments = Comment.objects.all().filter(post=posts).order_by('-timestamp')

    context = {

        'comments': comments,
        'posts': posts,
    }
    return render(request, 'comment_view.html', context)


def delete_post(request, pk):
    get_object_or_404(Post, pk=pk).delete()
    return redirect('user_profile')
