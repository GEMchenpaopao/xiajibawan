from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import redis
# Create your views here.

r = redis.Redis(password='123456')
def user_detail(request,uid):
    cache_key = 'user_%s'%uid
    if r.exists(cache_key):
        #读取缓存数据
        data = r.hgetall(cache_key)
        print(data)
        new_data = {k.decode():v.decode() for k,v in data.items()}
        username = new_data['username']
        age = new_data['age']
        result = 'cache:username is %s,age is %s'%(username,age)
        return HttpResponse(result)
    else:
        try:
            user = User.objects.get(id=uid)
        except:
            return HttpResponse('用户id错误')
        #写入缓存,为下一次访问提供方便
        r.hmset(cache_key,{'username':user.username,'age':user.age})
        #设置响应有效期
        r.expire(cache_key,30)
        #返回响应
        result = 'mysql:username is %s,age is %s'%(user.username,user.age)
        return HttpResponse(result)


def user_update(request,uid):

    age = request.GET.get('age',18)
    #1.查
    try:
        user = User.objects.get(id=uid)
    except:
        return HttpResponse('用户id有错误')
    #2.改
    user.age = age
    #3.存
    user.save()

    #清除缓存
    cache_key = 'user_%s' % uid
    r.delete(cache_key)
    return HttpResponse('更新用户的年龄成功')
