from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),

    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
	url(r'^event/new/$', views.create_new_event, name='create_new_event'),
	url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
	url(r'^drafts/$', views.event_draft_list, name='event_draft_list'),
	url(r'^event/(?P<pk>\d+)/create/$', views.event_create, name='event_create'),
	url(r'^event/(?P<pk>\d+)/remove/$', views.event_remove, name='event_remove'),
]
