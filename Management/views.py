from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count, Aggregate
# Create your views here.
from DoneWithIt.models import Item
from Messages.models import Chat
from PostsManagement.models import Post, Comment
from StudentGuildian.models import Article
from Userprofile.models import UserProfile, RequestPayment, PaymentDetail
import datetime


@staff_member_required
@login_required
def dashboard(request):
    posts = Post.objects.all().order_by('-timestamp')
    profile = UserProfile.objects.all().exclude(user=request.user)
    articles = Article.objects.all()
    messages = Chat.objects.all()
    items = Item.objects.all()
    new_posts = Post.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    new_profile = UserProfile.objects.all().exclude(user=request.user).filter(join__gte=datetime.date.today()) \
       .order_by('-join')
    new_articles = Article.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    new_messages = Chat.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    new_items = Item.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    rpay = RequestPayment.objects.all().filter(pending=True)
    fpay = RequestPayment.objects.all().filter(failed=True)
    ppay = RequestPayment.objects.all().filter(paid=True)
    context = {
        'articles': articles,
        'messages': messages,
        'items': items,
        'posts': posts,
        'profile': profile,

        'new_articles': new_articles,
        'new_messages': new_messages,
        'new_items': new_items,
        'new_posts': new_posts,
        'new_profile': new_profile,
        'rpay': rpay,
        'fpay': fpay,
        'ppay': ppay,

    }
    return render(request, 'dashboard.html', context)


@staff_member_required
@login_required
def kampus_users(request):
    user = get_user_model()
    users = user.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'Kampus_users.html', context)


@staff_member_required
@login_required
def new_user(request):
    users = UserProfile.objects.all().filter(join__gte=datetime.date.today()) \
        .order_by('-join')
    context = {
        'users': users,
    }
    return render(request, 'new_user.html', context)


@staff_member_required
@login_required
def user_details(request, pk):
    user_p = UserProfile.objects.get(user=pk)
    posts = Post.objects.all().filter(user=pk).order_by('-timestamp')
    total_like = posts.aggregate(total_like=Count('like'))['total_like']
    payment = PaymentDetail.objects.get(user=pk)
    p = payment.paid
    w = total_like * 10
    rw = w - p
    wallet = rw
    context = {
        'user_p': user_p,
        'posts': posts,
        'total_like': total_like,
        'wallet': wallet,
        'payment': payment,
    }
    return render(request, 'users_details.html', context)


@staff_member_required
@login_required
def kampus_post(request):
    post = Post.objects.all().order_by('-timestamp')
    context = {
        'post': post,
    }
    return render(request, 'Kampus_post.html', context)


@staff_member_required
@login_required
def new_post(request):
    post = Post.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    context = {
        'post': post,
    }
    return render(request, 'new_post.html', context)


@staff_member_required
@login_required
def donewithit_items(request):
    items = Item.objects.all().order_by('-timestamp')
    context = {
        'items': items,
    }
    return render(request, 'donwithit_items.html', context)


@staff_member_required
@login_required
def new_items(request):
    items = Item.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    context = {
        'items': items,
    }
    return render(request, 'new_items.html', context)


@staff_member_required
@login_required
def item_details(request, pk):
    items = Item.objects.get(pk=pk)
    context = {
        'items': items,
    }
    return render(request, 'ItemDetails.html', context)


@staff_member_required
@login_required
def articles_list(request):
    article = Article.objects.all().order_by('-timestamp')
    context = {
        'article': article,
    }
    return render(request, 'articles_list.html', context)


@staff_member_required
@login_required
def new_articles(request):
    article = Article.objects.all().filter(timestamp__gte=datetime.date.today()) \
        .order_by('-timestamp')
    context = {
        'article': article,
    }
    return render(request, 'new_article.html', context)


@staff_member_required
@login_required
def payment_request(request):
    rpay = RequestPayment.objects.all().filter(pending=True).order_by('-timestamp')
    context = {

        'rpay': rpay,

    }
    return render(request, 'payment_request.html', context)


@staff_member_required
@login_required
def failed_payment(request):
    fpay = RequestPayment.objects.all().filter(failed=True).order_by('-timestamp')
    context = {

        'fpay': fpay,

    }
    return render(request, 'failed_payment.html', context)


@staff_member_required
@login_required
def paid_user(request):
    fpay = RequestPayment.objects.all().filter(paid=True).order_by('-timestamp')

    total_paid = fpay.aggregate(total_paid=Sum('Amount'))['total_paid']
    context = {

        'fpay': fpay,
        'total_paid': total_paid,

    }
    return render(request, 'paid_user.html', context)


@staff_member_required
@login_required
def request_detail(request, pk):
    rpay = RequestPayment.objects.get(pk=pk)
    user = rpay.user
    acct = PaymentDetail.objects.get(user=user)
    profile = UserProfile.objects.get(user=user)

    context = {
        'rpay': rpay,
        'acct': acct,
        'profile': profile,

    }
    return render(request, 'request_detail.html', context)


@staff_member_required
@login_required
def paid(request, pk):
    rpay = RequestPayment.objects.get(pk=pk)
    rpay.pending = False
    rpay.paid = True
    rpay.failed = False
    rpay.save()
    user = rpay.user
    amount = rpay.Amount
    acct = PaymentDetail.objects.get(user=user)
    acct.paid += amount
    acct.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@staff_member_required
@login_required
def failed(request, pk):
    fpay = RequestPayment.objects.get(pk=pk)
    fpay.pending = False
    fpay.paid = False
    fpay.failed = True
    fpay.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
