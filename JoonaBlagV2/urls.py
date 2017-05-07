"""JoonaBlagV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.get_post, name='post'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload/file/$', views.file_upload, name='upload_file'),
    url(r'^post/(?P<post_id>[0-9]+)/comment$', views.post_comment, name='comment'),
    url(r'^accounts/login/$', views.do_login, name='login'),
    url(r'^accounts/logout/$', views.do_logout, name='logout'),
    url(r'^accounts/register/$', views.do_register, name='register'),
    url(r'^file/(?P<username>.+)/(?P<filename>[0-9]+\..{1,10})', views.get_file, name='file'),
    url(r'^admin/', admin.site.urls),
]
