from django.shortcuts import render, redirect
from django.contrib import messages
from ..log_reg.models import User
from .models import *
from django.core.urlresolvers import reverse

def index(request):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    context = {
        'users':User.objects.all().order_by('-created_at')[:3]
    }
    return render(request, "friend/index.html", context)

def logout(request):
    request.session.flush()
    return redirect('log_reg:index')

def pick_list(request, user_id):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    result = Friend.objects.pick_list(user_id)
    context = {
        'list':result
    }
    return render(request, "friend/add.html", context)

def friends_list(request, user_id):
    if not 'user_name' in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('log_reg:index')
    result = Friend.objects.show_friends(user_id)
    count = len(result)
    context = {
        'friends':result,
        'count':count,
    }
    return render(request, "friend/list.html", context)

def friendship(request, user_id, friend_id):
    Friend.objects.add_friendship(user_id, friend_id)
    return redirect(reverse('friend:pick_list', kwargs = {'user_id':user_id}))

def delete(request, user_id, friend_id):
    Friend.objects.delete_friendship(user_id, friend_id)
    return redirect(reverse('friend:friends_list', kwargs = {'user_id':user_id}))


# Create your views here.
