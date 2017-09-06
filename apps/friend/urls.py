from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^logout$', views.logout, name = "logout"),
    url(r'^pick_list/(?P<user_id>\d+)$', views.pick_list, name = "pick_list"),
    url(r'^friends_list/(?P<user_id>\d+)$', views.friends_list, name = "friends_list"),
    url(r'^friendship/(?P<user_id>\d+)/(?P<friend_id>\d+)$', views.friendship, name = "friendship"),
    url(r'^delete/(?P<user_id>\d+)/(?P<friend_id>\d+)$', views.delete, name = "delete"),
]