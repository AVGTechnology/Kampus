from django.db.models import Q
from django.shortcuts import render

from Userprofile.models import UserProfile
from .forms import *
from .models import *

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


@login_required
def sell_item(request):
    form = ItemForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('sell_item')
    else:
        form = ItemForm(user=request.user)

    return render(request, 'sell_item.html', {"form": form, })


@login_required
def details(request, pk):
    items = Item.objects.get(pk=pk)
    context = {
        'items': items,

    }
    return render(request, 'itemdetails_view.html', context)


@login_required
def account(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    items = Item.objects.all().filter(user=request.user).order_by('-timestamp')
    context = {
        'items': items,
        'profile': profile,

    }
    return render(request, 'account.html', context)


def view_account(request, pk):
    profile = UserProfile.objects.all().filter(user=pk)
    items = Item.objects.all().filter(user=pk).order_by('-timestamp')
    context = {
        'items': items,
        'profile': profile,

    }
    return render(request, 'view account.html', context)


def items(request):
    items = Item.objects.all().order_by('-timestamp')

    context = {
        'items': items,

    }
    return render(request, 'itemsfeed.html', context)


def delete_item(request, pk):
    get_object_or_404(Item, pk=pk).delete()
    return redirect('account')


def sold_item(request, pk):
    item = Item.objects.all().get(pk=pk)
    item.sold = True
    item.save()
    return redirect('account')


def notsold_item(request, pk):
    item = Item.objects.all().get(pk=pk)
    item.sold = False
    item.save()
    return redirect('account')


def search_item(request):
    query = request.GET.get('item')
    if query is not None:
        lookups = Q(item_name__icontains=query) | Q(item_dis__icontains=query)
        items = Item.objects.filter(lookups).distinct()

        context = {
            'items': items,
            'query': query,

        }
        return render(request, 'search_items.html', context)


def filter_item(request, Books):
    items = Item.objects.all().filter(category=Books)

    context = {
        'items': items,
        'str': Books,

    }
    return render(request, 'filter_items.html', context)
