from django.http import HttpResponse

#视图函数
#参数为请求对象
#返回值为请求对象

def page_2003(request):
    return HttpResponse('这是编号为2003的页面')
def page_2004(request):
    return HttpResponse('这是编号为2004的页面')
def page_index(request):
    return HttpResponse('<h1>不要找小火箭页面了,我是默认页面</h1>')
def page_num(request,num):
    return HttpResponse('path转换器:这是编号为%s的页面'%num)
def page_data(request,data):
    return HttpResponse('data%s'%data)
def page_zifuchuan(request,num1,zifuchuan,num2):
    if zifuchuan=='add': return HttpResponse('%s'%(num1+num2))
    elif zifuchuan=='sub': return HttpResponse('%s'%(num1-num2))
    elif zifuchuan=='mul': return HttpResponse('%s'%(num1*num2))
def birthday_view(request,y,m,d):
    print(request.method)
    print(request.path_info)
    return HttpResponse('您的生日为:%s年%s月%s日'%(y,m,d))

#测试request对象的使用,从request对象中获取客户端请求的信息
