import os

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
import json
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count, Aggregate
from django.views.decorators.csrf import csrf_exempt

from Management.models import AboutApp, AboutExcutives, LikePaymentUnit
from PostsManagement.models import Post
from .forms import *
from .models import *
from fcm_django.models import FCMDevice, FCMDeviceManager
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import JsonResponse
from django.core import serializers


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
    user = request.user
    if request.is_ajax():
        token = request.POST.get('token')
       # print(token)
        devices = FCMDevice.objects.filter(user=user.pk).exists()
        if devices:
            ufm = FCMDevice.objects.filter(user=user.pk)
            ufm.registration_id = token
            ufm.save()
        else:
            fcm = FCMDevice()
            fcm.name = user
            fcm.registration_id = token
            fcm.type = 'web'
            fcm.user = user.pk
            fcm.save()
            #print(token)
    return render(request, 'registration/login.html ')


@login_required
def create_profile(request):
    user = request.user
    form = UserProfileForm(request.POST, request.FILES, user=request.user)
    if form.is_valid():
        form.save()
        payment = PaymentDetail()
        payment.user = user
        payment.save()
        devices = FCMDevice.objects.filter(user=user.pk).exists()
        if devices:
            ufm = FCMDevice.objects.filter(user=user.pk)
            ufm.registration_id = ''
            ufm.save()
        else:
            fcm = FCMDevice()
            fcm.name = user
            fcm.registration_id = ''
            fcm.type = 'web'
            fcm.user = user.pk
            fcm.save()
        return redirect('user_profile')
    else:
        form = UserProfileForm(user=request.user)

    return render(request, 'create_profile.html', {"form": form, })


@login_required
def logout(request):
    return render(request, 'registration/logged_out.html ')


def about_kampus(request):
    services = AboutApp.objects.all()
    office = AboutExcutives.objects.all()

    context = {
        'services': services,
        'office': office,
    }
    return render(request, 'about_kampus.html', context)


def kampus_app(request):
    return render(request, 'Kampus_apps.html')


@login_required
def user_profile(request):
    user = request.user
    user_p = UserProfile.objects.all().filter(user=user)
    posts = Post.objects.all().filter(user=user).order_by('-timestamp')
    total_like = posts.aggregate(total_like=Count('like'))['total_like']

    return render(request, 'user_profile.html', {'user_p': user_p,
                                                 'posts': posts,
                                                 'total_like': total_like, })


@login_required
def profile_image_view(request, pk):
    user_p = UserProfile.objects.get(user=pk)

    return render(request, 'image_detail_view.html', {'user_p': user_p,
                                                      })


unit = LikePaymentUnit.unit


@login_required
def user_earning(request):
    likepayunit = LikePaymentUnit.objects.get(likeId=1)
    like_unit = likepayunit.unit
    pay_threshold = likepayunit.payment_threshold
    user = request.user
    user_p = UserProfile.objects.all().filter(user=user)
    posts = Post.objects.all().filter(user=user)
    total_like = posts.aggregate(total_like=Count('like'))['total_like']
    payment = PaymentDetail.objects.get(user=user)
    p = payment.paid
    w = total_like * like_unit
    rw = w - p
    wallet = rw
    requestpay = RequestPayment.objects.all().filter(user=user)

    return render(request, 'user_earning.html', {'user_p': user_p,
                                                 'posts': posts,
                                                 'total_like': total_like,
                                                 'wallet': wallet,
                                                 'payment': payment,
                                                 'pay_threshold': pay_threshold,
                                                 'like_unit': like_unit,
                                                 'requestpay': requestpay,
                                                 })


def requestpay(request):
    wallet = 0
    likepayunit = LikePaymentUnit.objects.get(likeId=1)
    like_unit = likepayunit.unit
    user = request.user
    posts = Post.objects.all().filter(user=request.user)
    total_like = posts.aggregate(total_like=Count('like'))['total_like']
    payment = PaymentDetail.objects.all().filter(user=user)
    for pay in payment:
        paid = pay.paid
        w = total_like * like_unit
        rw = w - paid
        wallet = rw
    request = RequestPayment.objects.all().filter(user=request.user)
    if request:

        rrequest = RequestPayment.objects.get(user=user)
        rrequest.Amount = wallet
        rrequest.pending = True
        rrequest.paid = False
        rrequest.failed = False
        rrequest.save()
        return redirect('user_earning')
    else:
        newrequest = RequestPayment()
        newrequest.Amount = wallet
        newrequest.user = user
        newrequest.paid = False
        newrequest.failed = False
        newrequest.pending = True
        newrequest.save()
        return redirect('user_earning')


def paymentform(request):
    form = PaymentForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return redirect('user_earning')
    else:
        form = PaymentForm()
    return render(request, 'paymentform.html', {'form': form})


@login_required
def edit_payment(request):
    user = get_object_or_404(PaymentDetail, user=request.user)
    payment_edit_form = PaymentEditForm(instance=user)
    if request.method == "POST":
        payment_edit_form = PaymentEditForm(request.POST, request.FILES, instance=user)
        if payment_edit_form.is_valid():
            payment_edit_form.save()
            return redirect('user_earning')

    context = {'payment_edit_form': payment_edit_form}

    return render(request, 'edit_payment.html', context)


@login_required
def edit_profile(request):
    user = request.user
    user_p = UserProfile.objects.all().filter(user=user)
    return render(request, 'edit_profile.html', {'user_p': user_p})


def view_user_profile(request, pk):
    user_p = UserProfile.objects.all().filter(user=pk)
    posts = Post.objects.all().filter(user=pk).order_by('-timestamp')

    return render(request, 'view_user_profile.html', {'user_p': user_p,
                                                      'posts': posts,
                                                      })


@login_required
def discover_account(request):
    account = UserProfile.objects.all().order_by('user').exclude(user=request.user)
    trendings = UserProfile.objects.all().order_by('user').exclude(user=request.user)

    # relationship = Relationship.objects.all()
    user_p = UserProfile.objects.get(user=request.user)
    prof = user_p.profession
    plookups = Q(profession__icontains=prof)
    prof = UserProfile.objects.filter(plookups).distinct().exclude(user=request.user)

    depts = user_p.dept
    dlookups = Q(profession__icontains=depts)
    depts = UserProfile.objects.filter(dlookups).distinct().exclude(user=request.user)

    trending = Trending.objects.get(Trend_number=1)

    context = {
        'account': account,
        'prof': prof,
        'depts': depts,
        'trending': trending,
        'trendings': trendings

    }
    return render(request, 'discover_account.html', context)


@login_required
def search_discover_account(request):
    query = request.GET.get('acct')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(profession__icontains=query) | Q(school__icontains=query) | \
                  Q(dept__icontains=query) | Q(phone__iexact=query)
        account = UserProfile.objects.filter(lookups).distinct()

        context = {
            'account': account,
            'query': query,

        }
        return render(request, 'search_discover_account.html', context)


@login_required
def discover_post(request):
    posts = Post.objects.all().order_by('-timestamp')
    trending = Trending.objects.get(Trend_number=1)
    context = {
        'posts': posts,
        'trending': trending,

    }
    return render(request, 'discover_post.html', context)


@login_required
def user_info(request):
    return render(request, 'user_info.html', )


@login_required
def search_discover_post(request):
    query = request.GET.get('post')
    if query is not None:
        lookups = Q(user__username__iexact=query) | Q(caption__icontains=query)
        posts = Post.objects.filter(lookups).order_by('-timestamp').distinct()

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

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
@login_required
def follow(request):
    pk = request.GET.get('pk', None)

    user = request.user
    u = UserProfile.objects.get(user=pk)

    print(u)

    auth_user = get_object_or_404(UserProfile, user=user)
    other_user = get_object_or_404(UserProfile, user=u.user)

    print(pk)
    if user in other_user.follower.all():
        other_user.follower.remove(user)
        auth_user.following.remove(u.user)
        unfollowed = 'unfollowed'
        data = {
            'unfollowed': unfollowed

        }

        return JsonResponse(data, status=200)
    else:
        auth_user.following.add(u.user)
        other_user.follower.add(user)
        followed = 'followed'
        data = {
            'followed': followed

        }

        return JsonResponse(data, status=200)


@login_required
def unfollow(request, pk):
    u = UserProfile.objects.get(user=pk)

    auth_user = get_object_or_404(UserProfile, user=request.user)
    other_user = get_object_or_404(UserProfile, user=u.user)

    auth_user.following.remove(u.user)
    other_user.follower.remove(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def followers(request, pk):
    follower = get_object_or_404(UserProfile, user=pk)

    context = {
        'follower': follower,

    }
    return render(request, 'followers.html', context)


@login_required
def followings(request, pk):
    following = get_object_or_404(UserProfile, user=pk)

    context = {
        'following': following,

    }
    return render(request, 'following.html', context)


# def edit_image(request):
#    return render(request, 'edit_image.html')


@login_required
def edit_image(request):
    user = get_object_or_404(UserProfile, user=request.user)
    image_edit_form = ImageEditForm(instance=user)
    if request.method == "POST":
        image_edit_form = ImageEditForm(request.POST, request.FILES, instance=user)
        if image_edit_form.is_valid():
            image_edit_form.save()

            return redirect('edit_profile')

    context = {'image_edit_form': image_edit_form}
    return render(request, 'edit_image.html', context)


@login_required
def edit_username(request):
    return render(request, 'edit_username.html')


@login_required
def edit_profession(request):
    return render(request, 'edit_profession.html')


@login_required
def edit_phone(request):
    return render(request, 'edit_phone.html')


@login_required
def edit_name(request):
    return render(request, 'edit_name.html')


@login_required
def edit_dept(request):
    return render(request, 'edit_dept.html')


@login_required
def edit_school(request):
    return render(request, 'edit_school.html')


@login_required
def username(request):
    uname = request.POST.get('username')
    user = get_user_model()
    profile = user.objects.get(username=request.user)
    profile.username = uname
    profile.save()

    return redirect('edit_profile')


@login_required
def profession(request):
    upro = request.POST.get('profession')
    profile = UserProfile.objects.get(user=request.user)
    profile.profession = upro
    profile.save()

    return redirect('edit_profile')


@login_required
def phone(request):
    up = request.POST.get('phone')
    profile = UserProfile.objects.get(user=request.user)
    profile.phone = up
    profile.save()

    return redirect('edit_profile')


@login_required
def image(request):
    upro = request.POST.get('image')
    profile = UserProfile.objects.get(user=request.user)
    profile.image = upro
    profile.save()

    return redirect('edit_profile')


@login_required
def dept(request):
    upro = request.POST.get('dept')
    profile = UserProfile.objects.get(user=request.user)
    profile.dept = upro
    profile.save()

    return redirect('edit_profile')


@login_required
def name(request):
    upro = request.POST.get('name')
    profile = UserProfile.objects.get(user=request.user)
    profile.full_name = upro
    profile.save()

    return redirect('edit_profile')


@login_required
def school(request):
    upro = request.POST.get('school')
    profile = UserProfile.objects.get(user=request.user)
    profile.school = upro
    profile.save()

    return redirect('edit_profile')


@csrf_exempt
def firebase_messaging_sw_js(request):
    filename = '/js/firebase-messaging-sw.js'
    jsfile = open(settings.APP_ROOT + filename, 'r')
    response = HttpResponse(content=jsfile)
    response['Content-Type'] = 'application/javascript'
    return response


@csrf_exempt
@login_required
def update_fcm_token(request):
    user = request.user
    token = request.GET.get('token', None)
    print(token)
    devices = FCMDevice.objects.filter(user=user).exists()
    if devices:
        ufm = FCMDevice.objects.get(user=user)
        ufm.registration_id = token
        ufm.save()
    else:
        fcm = FCMDevice()
        fcm.name = user
        fcm.registration_id = token
        fcm.type = 'web'
        fcm.user = user
        fcm.save()
        print(token)

    return JsonResponse({"token": token}, status=200)
