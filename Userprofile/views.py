from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from PostsManagement.models import Post
from .forms import *
from .models import *


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('create_profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    return render(request, 'registration/login.html ')


@login_required
def create_profile(request):
    form = UserProfileForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('user_profile')
    else:
        form = UserProfileForm(user=request.user)

    return render(request, 'create_profile.html', {"form": form, })


@login_required
def logout(request):
    return render(request, 'registration/logged_out.html ')


@login_required
def user_profile(request):
    user = request.user
    user_p = UserProfile.objects.all().filter(user=user)
    posts = Post.objects.all().filter(user=user)
    return render(request, 'user_profile.html', {'user_p': user_p,
                                                 'posts': posts})


@login_required
def view_user_profile(request, pk):
    user_p = UserProfile.objects.all().filter(user=pk)
    posts = Post.objects.all().filter(user=pk)
    return render(request, 'view_user_profile.html', {'user_p': user_p,
                                                      'posts': posts, })


def discover_account(request):
    account = UserProfile.objects.all().order_by('user').exclude(user=request.user)
    relationship = Relationship.objects.all()
    context = {
        'account': account,
        'relationship': relationship,
    }
    return render(request, 'discover_account.html', context)


def search_discover_account(request):
    query = request.GET.get('acct')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(profession__icontains=query)
        account = UserProfile.objects.filter(lookups).distinct()

        context = {
            'account': account,
            'query': query,

        }
        return render(request, 'search_discover_account.html', context)


def discover_post(request):
    posts = Post.objects.all().order_by('like')

    context = {
        'posts': posts,

    }
    return render(request, 'discover_post.html', context)


def search_discover_post(request):
    query = request.GET.get('post')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(caption__icontains=query)
        posts = Post.objects.filter(lookups).distinct()

        context = {
            'posts': posts,
            'query': query,

        }
        return render(request, 'search_discover_post.html', context)


@login_required
def follow(request, pk):
    u = UserProfile.objects.get(user=pk)

    auth_user = get_object_or_404(UserProfile, user=request.user)
    other_user = get_object_or_404(UserProfile, user=u.user)

    auth_user.following.add(u.user)
    other_user.follower.add(request.user)
    print(u.user)
    print(request.user)
    return redirect('discover_account')


@login_required
def unfollow(request, pk):
    u = UserProfile.objects.get(user=pk)

    auth_user = get_object_or_404(UserProfile, user=request.user)
    other_user = get_object_or_404(UserProfile, user=u.user)

    auth_user.following.remove(u.user)
    other_user.follower.remove(request.user)

    return redirect('discover_account')


def followers(request, pk):
    follower = get_object_or_404(UserProfile, user=pk)

    context = {
        'follower': follower,

    }
    return render(request, 'followers.html', context)


def followings(request, pk):
    following = get_object_or_404(UserProfile, user=pk)

    context = {
        'following': following,

    }
    return render(request, 'following.html', context)
