import json
from django.http import HttpRequest
from common.util.ResponseHelper import response
from rcms.models import Item, Project, Group
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
def create_group(request: HttpRequest):
    res = {}

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        name = body.get('name')
        if len(name.replace(" ", "")) <= 0:
            return response(-1, 'name error!')
        item = Group.objects.create(name=name)
        item.save()
        res['id'] = item.id
    else:
        return response(-1, "method error", res)
    return response(0, "ok", res)


@webuser_required(strict=True)
def update_group(request: HttpRequest):
    res = {}
    if (request.method == 'POST'):
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        try:
            item = Group.objects.get(id=body.get('id'))
        except ObjectDoesNotExist:
            return response(404, 'group not exist')
        item.name = body.get("name")
        if len(item.name.replace(" ", "")) <= 0:
            return response(-1, 'name error!')
        item.save()
    return response(0, "ok", res)


@webuser_required(strict=True)
def delete_group(request):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', -1))
        try:
            item = Group.objects.get(id=item_id)
            item.delete()
        except:
            return response(-1, "group id error")
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_group(request: HttpRequest):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', 0))
        try:
            item = Group.objects.get(id=item_id)
        except:
            return response(-1, "group id error")
        res = format(item)
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_all_groups(request: HttpRequest):
    res = {
        "groups": []
    }
    if request.method == 'GET':
        items = Group.objects.all()
        for i in items:
            res["groups"].append(format(i))
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_all_groups_with_projects(request: HttpRequest):
    t = {}
    res = []
    if request.method == 'GET':
        projects = Project.objects.all()
        for i in projects:
            if (i.group_id not in t):
                t[i.group_id] = {
                    'id': i.group_id,
                    'name': i.group.name,
                    'projects': [

                    ]
                }
            t[i.group_id]['projects'].append({
                "id": i.id,
                "name": i.name
            })
        for i in t.values():
            res.append(i)
    return response(0, "ok", res)
