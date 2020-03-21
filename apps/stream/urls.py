from django.conf.urls import url,include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^stream/list$', views.StreamList.as_view()),
    url(r'^stream/(?P<pk>[0-9]+)/$', views.StreamDetail.as_view()),
    url(r'^stream/edit/(?P<pk>[0-9]+)/$', views.StreamDetail.as_view()),
]
