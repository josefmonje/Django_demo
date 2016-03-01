from django.conf.urls import patterns, url
from .views import ProfileCreateView, ProfileDeleteView, ProfileDetailView, ProfileUpdateView


urlpatterns = patterns('',
    url(r'^$', ProfileDetailView.as_view(), name='detail'),
    url(r'^new/$', ProfileCreateView.as_view(), name='new'),
    url(r'^edit/$', ProfileUpdateView.as_view(), name='edit'),
    url(r'^delete/$', ProfileDeleteView.as_view(), name='delete'),
)
