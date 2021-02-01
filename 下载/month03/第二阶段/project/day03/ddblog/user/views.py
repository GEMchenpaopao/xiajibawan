import json

from django.utils.decorators import method_decorator

from tools.login_dec import login_check
from .models import UserProfile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import hashlib
import jwt
import time
from django.conf import settings
# Create your views here.
class UserView(View):
    #处理v1/users的 GET 请求
    def get(self,request,username=None):
        if username:
            #返回指定用户信息
            try:
                user = UserProfile.objects.get(username = username)
            except:
                result = {'code':10104,'error':'用户名称错误!'}
                return JsonResponse(result)
            if request.GET.keys():
                #获取指定信息
                data={}
                for k in request.GET.keys():
                    if k=='password':
                        continue
                    if hasattr(user,k):
                        data[k] = getattr(user,k)
                result = {'code':200,'username':username,
                          'data':data}
            else:
            #按格式返回用户信息
                result = {'code':200,'username':username,
                          'data':{'info':user.info,'sign':user.sign,
                                  'nickname':user.nickname,
                                  'avatar':str(user.avatar)}}
            return JsonResponse(result)
        else:
            return HttpResponse('-返回所有用户信息-')
    #处理 v1/users 的 POST 请求
    def post(self,request):
        #1. 获取前端给后端的json串
        json_str = request.body
        #2.把json串反序列化为对象
        json_obj = json.loads(json_str)
        #3.从对象[字典]中获取对象
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        #4数据检测
        #4.1 检测注册的用户名是否可以使用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code':10100,'error':'用户名已注册'}
            return  JsonResponse(result)
        #4.2两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        #4.3 添加密码的hash值
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()

        #5 插入数据[依然需要try]
        try:
            user = UserProfile.objects.create(username=username,
                                              password=password_h,
                                              email=email,
                                              phone=phone,
                                              nickname=username)
        except:
            result = {'code': 10102, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 6如何记住登录状态
        # 以前的云笔记当中,我们使用session保存登录状态
        #博客项目当中使用刚刚学习的token
        token = make_token(username)
        token = token.decode()
        return JsonResponse({'code':200,'username':username,'data':{'token':token}})
    #处理/v1/users/tedu的put请求
    @method_decorator(login_check)
    def put(self,request,username):
        #1 获取前端传递的json串
        json_str = request.body
        #2 将json串反序列化为对象
        json_obj = json.loads(json_str)
        #3 获取要修改的用户
        user = request.myuser
        #4 修改
        user.sign = json_obj['sign']
        user.nickname = json_obj['nickname']
        user.info = json_obj['info']
        #5 保存
        user.save()
        #6 返回
        result = {'code':200,'username':username}
        return JsonResponse(result)


def make_token(username,expire=3600*24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username':username,'exp':now+expire}
    #生成token
    return jwt.encode(payload,key,algorithm='HS256')
@login_check
def user_avatar(request,username):
    if request.method != 'POST':
        result = {'code':10105,'error':'只接受post请求'}
        return JsonResponse(result)
    #从request获取已经登陆的用户
    user = request.myuser
    #修改用户头像
    user.avatar = request.FILES['avatar']
    #保存
    user.save()
    #返回
    result = {'code':200,'username':user.username}
    return JsonResponse(result)

