from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




urlpatterns = [
    url(r'^auth/token/$', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^auth/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<user__username>[\w\-]+)/$', views.ProfileDetail.as_view()),
    url(r'^profile/edit/(?P<user__username>[\w\-]+)/$', views.ProfileUpdate.as_view()),
    url(r'^register', views.UserCreate.as_view(), name = 'account-create')
]
