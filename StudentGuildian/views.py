from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from Userprofile.models import UserProfile
from .models import *
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.


def articles(request):
    article = Article.objects.all().order_by('-timestamp')

    context = {
        'article': article
    }
    return render(request, 'articles.html', context)


def like(request):
    pass


def articles_details(request, pk):
    article = Article.objects.all().filter(pk=pk)

    context = {
        'article': article
    }
    return render(request, 'articles_details.html', context)


def articles_author(request, pk):
    user_p = UserProfile.objects.all().filter(user=pk)
    article = Article.objects.all().filter(user=pk).order_by('-timestamp')

    context = {
        'user_p': user_p,
        'article': article
    }
    return render(request, 'articles_author.html', context)


@login_required
def create_article(request):
    form = ArticleForm(request.POST, request.FILES,)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        messages.success(request, 'Article was created Successfully!! .')
        messages.success(request, 'Create more Articles!')
        return redirect('articles')
    else:
        form = ArticleForm()
    messages.info(request, 'Creating Article please wait...')
    return render(request, 'create_article.html', {"form": form, })


@login_required
def add_article(request):
    body = request.POST.get('body')
    title = request.POST.get('title')
    user = request.user

    article = Article()
    article.title = title
    article.body = body
    article.user = user
    article.save()

    return redirect('articles')


def search_article(request):
    query = request.GET.get('article')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(title__icontains=query)
        article = Article.objects.filter(lookups).distinct()

        context = {
            'query': query,
            'article': article,

        }
        return render(request, 'search_article.html', context)


@login_required
def delete_article(request, pk):
    get_object_or_404(Article, pk=pk).delete()
    return redirect('articles')