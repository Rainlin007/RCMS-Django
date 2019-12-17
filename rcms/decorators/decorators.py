from rcms.models import User
from common.util.ResponseHelper import response


# 验证微信用户，获取user到wxuser
def wxuser_required(strict=True):
    def validate(view_fn):
        def wrapper_fn(request, *args, **kwargs):
            token = request.header.get('token')
            if not token and strict:
                return response(403, 'not login', {})
            try:
                user = User.objects.get(token=token)
            except User.DoesNotExist:
                user = None
                if strict:
                    return response(403, 'not login', {})

            request.wxuser = user
            return view_fn(request, *args, **kwargs)

        return wrapper_fn

    return validate


# 验证web用户，获取user到webuser
def webuser_required(strict=True):
    def validate(view_fn):
        def wrapper_fn(request, *args, **kwargs):
            token = request.COOKIES.get('token')
            if not token and strict:
                return response(403, 'not login', {})
            try:
                user = User.objects.get(token=token)
            except User.DoesNotExist:
                user = None
                if strict:
                    return response(403, 'not login', {})

            request.webuser = user
            return view_fn(request, *args, **kwargs)

        return wrapper_fn

    return validate
