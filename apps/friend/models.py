from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import User

class FriendManager(models.Manager):
    def pick_list(self, user_id):
        me = User.objects.get(id = user_id)
        other_users = User.objects.all().exclude(id = user_id)
        the_rest = []
        for each in other_users:
            the_rest.append(each)

        friendships = Friend.objects.filter(first_friend = me)
        my_friends = []
        for each in friendships:
            my_friends.append(each.second_friend)
        
        non_friends = []
        for each in the_rest:
            if each not in my_friends:
                non_friends.append(each)
        return non_friends

    def show_friends(self, user_id):
        me = User.objects.get(id = user_id)
        my_friends = []
        friends = Friend.objects.filter(first_friend = me)
        for each in friends:
            my_friends.append(each.second_friend)
        return my_friends

    def add_friendship(self, user_id, friend_id):
        user = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        Friend.objects.create(first_friend=user, second_friend=friend)
        Friend.objects.create(first_friend=friend, second_friend=user)
 
    def delete_friendship(self, user_id, friend_id):
        user = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        friendship1 = Friend.objects.get(first_friend=user, second_friend=friend)
        friendship2 = Friend.objects.get(first_friend=friend, second_friend=user)
        friendship1.delete()
        friendship2.delete()



class Friend(models.Model):
    first_friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "accepter")
    second_friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "requester")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = FriendManager()
# Create your models here.
