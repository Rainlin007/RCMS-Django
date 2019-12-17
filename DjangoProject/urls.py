"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import rcms.views

urlpatterns = [
    path('django/admin/', admin.site.urls),

    # cms接口
    url(r'rcms/item/create$', rcms.views.create_item),
    url(r'rcms/item/read$', rcms.views.read_item),
    url(r'rcms/item/update$', rcms.views.update_item),
    url(r'rcms/item/delete$', rcms.views.delete_item),

    url(r'rcms/item/read_all$', rcms.views.read_all_item),

    url(r'rcms/project/create$', rcms.views.create_project),
    url(r'rcms/project/read$', rcms.views.read_project),
    url(r'rcms/project/update$', rcms.views.update_project),
    url(r'rcms/project/delete$', rcms.views.delete_project),

    url(r'rcms/project/read_all$', rcms.views.read_all_project),

    url(r'rcms/group/create$', rcms.views.create_group),
    url(r'rcms/group/read$', rcms.views.read_group),
    url(r'rcms/group/update$', rcms.views.update_group),
    url(r'rcms/group/delete$', rcms.views.delete_group),

    url(r'rcms/group/read_all$', rcms.views.read_all_group),
    url(r'rcms/group/read_all_projects$', rcms.views.read_all_groups_with_projects),

    url(r'rcms/login', rcms.views.login),

    # 接口发布url，应放于末尾匹配
    url(r'p/.*', rcms.views.get_publish_item)

]
