# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from werobot.contrib.django import make_view
from . import views

from .robot import robot

urlpatterns = [
    url(r'^$', views.home, name="site_home"),
    url(r'^MP_verify_kn6YuZIRpnYWeVCO.txt$', views.wx_js, name="wx_js"),
    url(r'^admin/', admin.site.urls),
    url(r'^robot/', make_view(robot)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^xyf/', include('xyf.urls')),
    url(r'^jinkong/', include('jinkong.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
