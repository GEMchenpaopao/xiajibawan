from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = '''
<form method='get' action="/test_get">
    <p>
    姓名:<input type="text" name="uname">
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
</form>
'''
html2 = '''
<form method='post' action="/test_post">
    <p>
    姓名:<input type="text" name="uname">
    </p>
    <p>
        <input type="submit" value="提交">
    </p>
</form>
'''



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showData(self):
        return '姓名:%s,age:%s'%(self.name,self.age)

def test_get(request):
    #后端收到客户端提交的查询字符串打印
    #1.要求查询字符串中存在名称为uname的数据,如果没有,报错
    # uname = request.GET['uname']
    #2.换一种方式获取,试着获取,没有也不报错,值为None而已
    #uname = request.GET.get('uname')
    #3.试着获取,有值拿值,没有值,使用默认值
    uname = request.GET.get('uname','tedu')
    print(uname)
    #4.如果同一个名称有多个值
    print(request.GET.getlist('a'))
    return HttpResponse(html)

def test_post(request):
    if request.method =='GET':
        return HttpResponse(html2)
    elif request.method =='POST':
        uname = request.POST['uname']
        return HttpResponse('杭州欢迎您%s'%uname)

def birthday(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    return HttpResponse('您的生日是:%s年%s月%s日'%(year,month,day))
def Hello():
    return '杭州欢迎您!'

def test_html(request):
    #返回一个模板页.方式一
    # t=loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    #return render(request,'test_html.html')
    # 方式二
    # dict1 = {}
    # dict1['name']='aid2010'
    # dict1['count']='300'
    # dict1['citys']=['北京','上海','天津','重庆']
    # dict1['distribute'] = {'北京':100,'上海':100,'天津':50,'重庆':50}
    # dict1['p1']= Person('迪迦',25)
    # dict1['function1'] = Hello
    # dict1['script'] = '<script>alert("Hello World")</script>'
    # return render(request,'test_html.html',dict1)


    #3.终极解决方案

    name='aid2010'
    count=300
    citys=['北京','上海','天津','重庆']
    distribute = {'北京':100,'上海':100,'天津':50,'重庆':50}
    p1= Person('迪迦',25)
    function1 = Hello
    script = '<script>alert("Hello World")</script>'
    persons = ['关羽','张飞','赵云','马超','黄忠']
    persons = []
    return render(request,'test_html.html',locals())

def test_calc(request):
    if request.method =='GET':
        return render(request,'test_calc.html')
    elif request.method =='POST':
        x=request.POST['x']
        y=request.POST['y']
        if not x or not y:
            return HttpResponse('请输入数据')
        try:
            x=int(x)
            y=int(y)
        except:
            return HttpResponse('请输入一个整数值')
        op=request.POST['op']
        if op == 'add':
            res = x+y
        elif op=='sub':
            res = x-y
        elif op=='mul':
            res=x*y
        else :
            res = x/y
        return render(request,'test_calc.html',locals())