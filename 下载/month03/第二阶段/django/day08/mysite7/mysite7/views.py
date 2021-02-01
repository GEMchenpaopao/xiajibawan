


import time
import os
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import csv
#在视图函数中如果使用当前的配置文件时
#django要求我们导入的是他的内置的settings,而不是我们这个
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from test_upload.models import Content


@cache_page(100)
def test_cache(request):
    t1 = time.time()
    time.sleep(3)
    return HttpResponse('time is %s'%t1)

def test_mw(request):

    print('my view in')
    return HttpResponse('my middlware view!')

def test_csrf(request):
    if request.method == 'GET':
        return render(request,'test_csrf.html')
    elif request.method == 'POST':
        username = request.POST['username']
        return HttpResponse('username is %s'%username)

def test_page(request):
    #1 要分页的数据
    list1 = ['a','b','c','d','e']
    #2 创建Paginator对象
    paginator = Paginator(list1,2)
    #3 从查询字符串中获取当前页码
    cur_page = request.GET.get('page',1)
    #4 创建page
    page = paginator.page(cur_page)
    #5 返回页面
    return render(request,'test_page.html',locals())

def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    #创建一个csv的写入器
    writer = csv.writer(response)
    writer.writerow(['图书编号','图书名称'])
    #准备数据
    all_books = [
        {'id':1,'title':'python'},
        {'id': 2, 'title': 'java'},
        {'id': 3, 'title': 'c++'},
    ]
    #写入数据
    for b in all_books:
        writer.writerow([b['id'],b['title']])
    return response

@csrf_exempt
def test_upload(request):
    if request.method == "GET":
        return render(request,'test_upload.html')
    elif request.method == "POST":
        #获取文件对象
        afile = request.FILES['myfile']
        #获取表单元素的值
        title = request.POST['title']
        # # 生成一个服务器端文件的全路径 GUID:(全局唯一标识符)作为文件名的一部分防止重名
        # filename = os.path.join(settings.MEDIA_ROOT,afile.name)
        # with open(filename,'wb') as f:
        #     #获取文件内容
        #     data = afile.file.read()
        #     #写入到服务器
        #     f.write(data)
        # result = '文件%s上传成功!文件描述:%s'%(afile.name,title)
        # return HttpResponse(result)


        #第二种文件
        Content.objects.create(title=title,myfile=afile)
        result = '文件%s上传成功!文件描述:%s'%(afile.name,title)
        return HttpResponse(result)

