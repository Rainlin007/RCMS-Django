import json
from django.http import HttpRequest
from common.util.ResponseHelper import response


# 要求提供request.body，转换body至request.json中
def json_required(view_fn):
    def wrapper_fn(request: HttpRequest, *args, **kwargs):
        pass
        try:
            request.json = json.loads(request.body)
        except:
            return response(-1, 'JSON error')
        return view_fn(request, *args, **kwargs)

    return wrapper_fn
