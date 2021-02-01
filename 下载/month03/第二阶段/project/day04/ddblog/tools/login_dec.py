import jwt
from django.http import JsonResponse
from django.conf import settings
from user.models import UserProfile
def login_check(func):
    def wrap(request,*args,**kwargs):
        # 在请求对象中获取前端提交过来的token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code':403,'error':'请登录!'}
            return JsonResponse(result)
        #token的校验
        try:
            payload = jwt.decode(token,settings.JWT_TOKEN_KEY,algorithm='HS256')
        except:
            result = {'code':403,'error':'请登录!'}
            return JsonResponse(result)
        #从结果中获取私有申明
        username = payload['username']
        #根据用户名称获取用户对象
        user = UserProfile.objects.get(username = username)
        #将用户对象作为request的附加属性
        request.myuser = user
        #调用所修饰的函数
        return func(request,*args,**kwargs)
    return wrap