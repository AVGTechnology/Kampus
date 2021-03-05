from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from Userprofile.models import UserProfile
from .forms import ChatForm
from .models import *


def chat_page(request, pk):
    recipient = UserProfile.objects.get(user=pk)
    user = get_user_model()
    r = user.objects.get(pk=pk)
    received_msg = Chat.objects.all().filter(recipient=request.user).filter(sender=r)
    sent_msg = Chat.objects.all().filter(sender=request.user).filter(recipient=r)
    megs = received_msg | sent_msg.order_by('timestamp')

    context = {
        'megs': megs,
        'recipient': recipient,
        'received_msg': received_msg,
        'sent_msg': sent_msg,

    }
    return render(request, 'chat_page.html', context)


def received_list(request):
    megs = Chat.objects.all().filter(recipient=request.user).order_by('-timestamp')

    context = {
        'megs': megs,

    }
    return render(request, 'received_list.html', context)


def sent_list(request):
    megs = Chat.objects.all().filter(sender=request.user).order_by('-timestamp')

    context = {
        'megs': megs,

    }
    return render(request, 'sent_list.html', context)


def message_user_list(request):
    users = UserProfile.objects.all().order_by('user').exclude(user=request.user)

    context = {
        'users': users,

    }
    return render(request, 'message_user_list.html', context)


def search_message_user_list(request):
    query = request.GET.get('acct')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(profession__icontains=query)
        account = UserProfile.objects.filter(lookups).distinct()

        context = {
            'account': account,
            'query' : query,

        }
        return render(request, 'search_message_user_list.html', context)
    else:

        return redirect('message_user_list')


def send_chat(request, pk):
    chats = request.POST.get('chats')
    user = get_user_model()
    receiver = user.objects.get(pk=pk)
    chat = Chat()
    chat.recipient = receiver
    chat.sender = request.user
    chat.text = chats
    chat.save()

    return redirect('chat_page', pk)
