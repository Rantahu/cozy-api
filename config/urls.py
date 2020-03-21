"""cozy_boards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.apps import apps

boards_name = apps.get_app_config('boards').verbose_name
exchange_name = apps.get_app_config('exchange').verbose_name
accounts_name = apps.get_app_config('accounts').verbose_name
stream_name = apps.get_app_config('stream').verbose_name

from apps.boards import views as boards_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^boards/', include(('apps.boards.urls', boards_name), namespace='boards')),
    url(r'^exchange/', include(('apps.exchange.urls', exchange_name), namespace='exchange')),
    url(r'^stream/', include(('apps.stream.urls', stream_name), namespace='stream')),
    url(r'^', include(('apps.accounts.urls', accounts_name), namespace='accounts'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
'''
