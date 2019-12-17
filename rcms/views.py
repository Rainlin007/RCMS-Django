from django.views.decorators.cache import cache_page

import rcms.viewmodule.ItemManager
import rcms.viewmodule.ProjectManager
import rcms.viewmodule.GroupManager
import rcms.viewmodule.UserManager


# item的增删查改
def create_item(request):
    return rcms.viewmodule.ItemManager.create_item(request)


def delete_item(request):
    return rcms.viewmodule.ItemManager.delete_item(request)


def read_item(request):
    return rcms.viewmodule.ItemManager.read_item(request)


def update_item(request):
    return rcms.viewmodule.ItemManager.update_item(request)


def read_all_item(request):
    return rcms.viewmodule.ItemManager.read_all_items(request)


# project的增删查改
def create_project(request):
    return rcms.viewmodule.ProjectManager.create_project(request)


def delete_project(request):
    return rcms.viewmodule.ProjectManager.delete_project(request)


def read_project(request):
    return rcms.viewmodule.ProjectManager.read_project(request)


def update_project(request):
    return rcms.viewmodule.ProjectManager.update_project(request)


def read_all_project(request):
    return rcms.viewmodule.ProjectManager.read_all_projects(request)


# group的增删查改
def create_group(request):
    return rcms.viewmodule.GroupManager.create_group(request)


def delete_group(request):
    return rcms.viewmodule.GroupManager.delete_group(request)


def read_group(request):
    return rcms.viewmodule.GroupManager.read_group(request)


def update_group(request):
    return rcms.viewmodule.GroupManager.update_group(request)


def read_all_group(request):
    return rcms.viewmodule.GroupManager.read_all_groups(request)


def read_all_groups_with_projects(request):
    return rcms.viewmodule.GroupManager.read_all_groups_with_projects(request)


# user相关
def login(request):
    return rcms.viewmodule.UserManager.login(request)


# 缓存
@cache_page(cache='default', key_prefix='rcms', timeout=60)
def get_publish_item(request):
    return rcms.viewmodule.ItemManager.get_publish_item(request)
