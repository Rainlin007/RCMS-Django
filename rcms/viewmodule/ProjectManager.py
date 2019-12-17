import json
from django.http import HttpRequest
from common.util.ResponseHelper import response
from rcms.models import Project
from rcms.decorators.decorators import webuser_required
from django.core.exceptions import ObjectDoesNotExist


def format(item):
    item_info = {
        'id': item.id,
        'created_at': item.created_at,
        'updated_at': item.updated_at,
        'name': item.name,
    }
    return item_info


@webuser_required(strict=True)
def create_project(request: HttpRequest):
    res = {}
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        name = body.get('name')
        if len(name.replace(" ", "")) <= 0:
            return response(-1, 'name error')
        group_id = body.get('group_id')
        item = Project.objects.create(name=name, group_id=group_id)
        item.save()
        res['id'] = item.id
    else:
        return response(-1, "method error", res)
    return response(0, "ok", res)


@webuser_required(strict=True)
def update_project(request: HttpRequest):
    res = {}
    if (request.method == 'POST'):
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        try:
            item = Project.objects.get(id=body.get('id'))
        except ObjectDoesNotExist:
            return response(404, 'project not exist')
        item.name = body.get("name")
        if len(item.name.replace(" ", "")) <= 0:
            return response(-1, 'name error')
        item.save()
    return response(0, "ok", res)


@webuser_required(strict=True)
def delete_project(request):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', -1))
        try:
            item = Project.objects.get(id=item_id)
            item.delete()
        except:
            return response(-1, "project id error")
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_project(request: HttpRequest):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', 0))
        try:
            item = Project.objects.get(id=item_id)
        except:
            return response(-1, "project id error")
        res = format(item)
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_all_projects(request: HttpRequest):
    res = {
        "projects": []
    }
    if request.method == 'GET':
        group_id = int(request.GET.get('id', -1))
        if (group_id == -1):
            return response(-1, "group id error")
        items = Project.objects.filter(group_id=group_id)
        for i in items:
            res["projects"].append(format(i))
    return response(0, "ok", res)
