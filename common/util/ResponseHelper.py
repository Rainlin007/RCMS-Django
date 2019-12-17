import json

from django.http import JsonResponse


# 通用返回数据结构
def response(errcode=0, errmsg='', data={}, cookie=None):
    res = JsonResponse({
        'errcode': errcode,
        'errmsg': errmsg,
        'data': data
    })
    if (cookie != None):
        for i in cookie:
            res.set_cookie(i, cookie[i])
    return res

