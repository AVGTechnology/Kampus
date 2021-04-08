from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from fcm_django.models import FCMDevice

from Userprofile.models import UserProfile
from .forms import ChatForm
from .models import *


@login_required
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


@login_required
def received_list(request):
    megs = Chat.objects.all().filter(recipient=request.user).order_by('-timestamp')

    context = {
        'megs': megs,

    }
    return render(request, 'received_list.html', context)


@login_required
def sent_list(request):
    megs = Chat.objects.all().filter(sender=request.user).order_by('-timestamp')

    context = {
        'megs': megs,

    }
    return render(request, 'sent_list.html', context)


@login_required
def message_user_list(request):
    users = UserProfile.objects.all().order_by('user').exclude(user=request.user)

    context = {
        'users': users,

    }
    return render(request, 'message_user_list.html', context)


@login_required
def search_message_user_list(request):
    query = request.GET.get('acct')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(profession__icontains=query)
        account = UserProfile.objects.filter(lookups).distinct()

        context = {
            'account': account,
            'query': query,

        }
        return render(request, 'search_message_user_list.html', context)
    else:

        return redirect('message_user_list')


@login_required
def send_chat(request, pk):
    chats = request.POST.get('chats')
    user = get_user_model()
    receiver = user.objects.get(pk=pk)
    chat = Chat()
    chat.recipient = receiver
    chat.sender = request.user
    chat.text = chats
    chat.save()
    sender = request.user
    device = FCMDevice.objects.get(user=receiver)
    device.send_message(title=f'{sender} sent you a message', body=f'{chats} ',
                        icon='static/images/logo.png',
                        data={"Details": "Details"})

    return redirect('chat_page', pk)
