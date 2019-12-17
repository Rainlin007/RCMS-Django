import json
from django.http import HttpRequest, HttpResponse
from common.util.ResponseHelper import response
from rcms.models import Item, Project, Group, User
from rcms.decorators.decorators import webuser_required
from django.core.exceptions import ObjectDoesNotExist


def format(item):
    item_info = {
        'id': item.id,
        'created_at': item.created_at,
        'updated_at': item.updated_at,
        'account': item.name,
        'password': item.name,
    }
    return item_info


@webuser_required(strict=False)
def create_user(request: HttpRequest):
    res = {}

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        account = body.get('account')
        password = body.get('password')
        user = User.objects.create(account=account, password=password)
        user.save()
        res['id'] = user.id
    else:
        return response(-1, "method error", res)
    return response(0, "ok", res)


@webuser_required(strict=False)
def update_user(request: HttpRequest):
    res = {}
    if (request.method == 'POST'):
        try:
            body = json.loads(request.body)
        except:
            return response(-1, 'json load error')
        try:
            user = User.objects.get(id=body.get('id'))
        except ObjectDoesNotExist:
            return response(404, 'user not exist')
        user.account = body.get("account")
        user.password = body.get("password")
        user.save()
    return response(0, "ok", res)


@webuser_required(strict=False)
def delete_user(request):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', -1))
        try:
            item = User.objects.get(id=item_id)
            item.delete()
        except:
            return response(-1, "user_id error")
    return response(0, "ok", res)


@webuser_required(strict=False)
def read_user(request: HttpRequest):
    res = {}
    if request.method == 'GET':
        item_id = int(request.GET.get('id', 0))
        try:
            item = User.objects.get(id=item_id)
        except:
            return response(-1, "user_id error")
        res = format(item)
    return response(0, "ok", res)


def verify(json, keys):
    for key in keys:
        if (key not in json):
            return False
    return True


@webuser_required(strict=False)
def login(request: HttpRequest):
    try:
        body = json.loads(request.body)
    except:
        return response(-1, 'json load error')
    if not verify(body, ["account", "password"]):
        return response(-2, "params error")
    account = body.get("account")
    password = body.get("password")
    t = User.objects.filter(account=account, password=password)
    if len(t) == 0:
        return response(-3, "account or password error")
    cookie = {
        'token': t[0].token
    }
    return response(0, 'ok', {"account": account}, cookie)
