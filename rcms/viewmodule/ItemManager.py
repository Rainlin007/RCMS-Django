import json
from django.http import HttpRequest
from common.util.ResponseHelper import response
from rcms.models import Item
from rcms.decorators.decorators import webuser_required
from django.core.exceptions import ObjectDoesNotExist


def format_item(item):
    value = item.value
    item_info = {
        'id': item.id,
        'created_at': item.created_at,
        'updated_at': item.updated_at,
        'comment': item.comment,
        'path': item.path,
        'value': value
    }
    return item_info


@webuser_required(strict=True)
def create_item(request: HttpRequest):
    res = {}

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        path = body.get('path')
        path = path.replace(" ", "")
        if len(path) == 0:
            return response(-1, 'path error!')
        if path[0] != '/':
            path = "/" + path
        comment = body.get('comment')
        value = body.get('value')
        project_id = body.get("project_id")
        item = Item.objects.create(path=path, comment=comment, value=value, project_id=project_id)
        item.save()
        res['id'] = item.id
    else:
        return response(-1, "method error", res)
    return response(0, "ok", res)


@webuser_required(strict=True)
def update_item(request: HttpRequest):
    res = {}
    if (request.method == 'POST'):
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        try:
            item = Item.objects.get(id=body.get('id'))
        except ObjectDoesNotExist:
            return response(404, 'item not exist')

        path = body.get("path")
        path = path.replace(" ", "")
        if len(path) == 0:
            return response(-1, 'path error!')
        if path[0] != '/':
            path = "/" + path
        item.path = path
        item.comment = body.get("comment")
        item.value = body.get("value")
        item.save()
    return response(0, "ok", res)


@webuser_required(strict=True)
def delete_item(request):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', -1))
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
        except:
            return response(-1, "item_id error")
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_item(request: HttpRequest):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', 0))
        try:
            item = Item.objects.get(id=item_id)
        except:
            return response(-1, "item_id error")
        res = format_item(item)
    return response(0, "ok", res)


@webuser_required(strict=True)
def read_all_items(request: HttpRequest):
    res = {
        "items": []
    }
    if request.method == 'GET':
        project_id = int(request.GET.get('id', -1))
        if (project_id == -1):
            return response(-1, "project_id error")
        items = Item.objects.filter(project=project_id)
        for i in items:
            res["items"].append(format_item(i))
    return response(0, "ok", res)


@webuser_required(strict=False)
def get_publish_item(request: HttpRequest):
    res = {}
    path = request.path_info[2:]
    if request.method == 'GET':
        items = Item.objects.filter(path=path)
        if (len(items) == 0):
            return response(-1, "path error")

        text = items[0].value
        try:
            res = json.loads(text)
        except:
            res = text

    return response(0, "ok", res)
