
from django.conf.urls import url
from django.contrib import admin
from mysiteapp.views import UserList, UserProfile, EventDetail, EventList, VideoDetail, EventPage, VideoList, ImageDetail, ImageList
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users_list/$', UserList.as_view(), name='users_list'),
    url(r'^users_list/(?P<pk>[0-9]+)/$', UserProfile.as_view(), name='user_profile'),
    url(r'^events_list/$', EventList.as_view(), name='events_list'),
    url(r'^events_list/(?P<pk>[0-9]+)/$', EventDetail.as_view(), name='event', ),
    url(r'^images_list/$', ImageList.as_view(), name='images_list'),
    url(r'^images_list/(?P<pk>[0-9]+)/$', ImageDetail.as_view(), name='image'),
    url(r'^videos_list/$', VideoList.as_view(), name='videos_list'),
    url(r'^videos_list/(?P<pk>[0-9]+)/$', VideoDetail.as_view(), name='video'),
    url(r'^event/(?P<pk>[0-9]+)/$', EventPage.as_view(), name='event_page'),
    url(r'^$', RedirectView.as_view(url='/event/8')),
]
