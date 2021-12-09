from django.db.models import Q
from django.shortcuts import render
from fcm_django.models import FCMDevice

from Userprofile.models import UserProfile
from .forms import *
from .models import Product
from PostsManagement.models import Post

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render
from django.views.generic.list import ListView


# Create your views here.


@login_required
def sell_item(request):
    form = ItemForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        instance = form.save()
        messages.success(request, 'Item added Successfully!! .')
        messages.success(request, 'Add More Items...')
        n_item = Product.objects.get(pk=instance.pk)
        name = n_item.item_name
        seller = n_item.user
        image = n_item.first_image
        location = n_item.location
        price = n_item.price
        free = n_item.free
        contact = n_item.contact
        if price > 0:
            device = FCMDevice.objects.all()
            device.send_message(title=f'{seller}  want to sell {name} on DoneWithIt ', body=f'For ₦{price}, location is '
                                f'at {location}. Check App for more details...'
                                'https://kampusng.com{% url "view_user_profile" user.pk %}'
                                ,
                                icon='static/images/logo.png',
                                data={"Details": "Details"})
        elif free:
            device = FCMDevice.objects.all()
            device.send_message(title=f'{seller} want to give out {name} on DoneWithIt ', body=f'For FREE, locations '
                                                                                               f'is  at {location}. Check App for more details... ',
                                icon='static/images/logo.png',
                                data={"Details": "Details"})
        elif contact:
            device = FCMDevice.objects.all()
            device.send_message(title=f'{seller} want to sell {name} on DoneWithIt ', body=f'Contact for price, '
                                                                                           f'location is at {location}. Check App for more details... ',
                                icon='static/images/logo.png',
                                data={"Details": "Details"})

        return redirect('donewithit')
    else:
        form = ItemForm(user=request.user)
        messages.info(request, 'Posting please wait...')
    return render(request, 'sell_item.html', {"form": form, })


@login_required
def details(request, pk):
    items = Product.objects.get(pk=pk)
    context = {
        'items': items,

    }
    return render(request, 'itemdetails_view.html', context)


@login_required
def account(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    items = Product.objects.all().filter(user=request.user).order_by('-timestamp')
    context = {
        'items': items,
        'profile': profile,

    }
    return render(request, 'account.html', context)


def view_account(request, pk):
    profile = UserProfile.objects.all().filter(user=pk)
    items = Product.objects.all().filter(user=pk).order_by('-timestamp')
    context = {
        'items': items,
        'profile': profile,

    }
    return render(request, 'view account.html', context)


class Item(ListView):
    model = Product
    paginate_by = 3
    context_object_name = 'items'
    template_name = 'itemsfeed.html'
    ordering = ['-timestamp']


def delete_item(request, pk):
    get_object_or_404(Product, pk=pk).delete()
    return redirect('account')


def sold_item(request, pk):
    item = Product.objects.all().get(pk=pk)
    item.sold = True
    item.save()
    return redirect('account')


def notsold_item(request, pk):
    item = Product.objects.all().get(pk=pk)
    item.sold = False
    item.save()
    return redirect('account')


def search_item(request):
    query = request.GET.get('item')
    if query is not None:
        lookups = Q(item_name__icontains=query) | Q(item_dis__icontains=query)
        items = Product.objects.filter(lookups).distinct()

        context = {
            'items': items,
            'query': query,

        }
        return render(request, 'search_items.html', context)


def filter_book(request):
    items = Product.objects.all().filter(category='Book')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_phone(request):
    items = Product.objects.all().filter(category='Phone')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_computer(request):
    items = Product.objects.all().filter(category='Computer')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_appliances(request):
    items = Product.objects.all().filter(category='Appliances')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_gadget(request):
    items = Product.objects.all().filter(category='Gadget')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_furniture(request):
    items = Product.objects.all().filter(category='Furniture')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_apartment(request):
    items = Product.objects.all().filter(category='Apartment')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_book(request):
    items = Product.objects.all().filter(category='Book')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_clothing(request):
    items = Product.objects.all().filter(category='Clothing')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_vehicle(request):
    items = Product.objects.all().filter(category='Vehicle')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_kitchen(request):
    items = Product.objects.all().filter(category='Kitchen')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)


def filter_others(request):
    items = Product.objects.all().filter(category='Others')

    context = {
        'items': items,

    }
    return render(request, 'filter_items.html', context)
