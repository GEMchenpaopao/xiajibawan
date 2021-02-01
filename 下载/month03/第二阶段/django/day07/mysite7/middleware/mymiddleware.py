from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import  re
class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response
class MyMiddleWare2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法2 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法2 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法2 process_response 被调用")
        return response
class MyMw(MiddlewareMixin):
    visit_times = {}
    def process_request(self,request):
        #获取客户端IP地址
        cip = request.META['REMOTE_ADDR']
        #只有path以/test开头的才做限制
        if not re.match(r'^/test',request.path_info):
            return
        #获取键为cip的访问次数
        times = self.visit_times.get(cip,0)
        if times >= 5:
            return HttpResponse('no way!')
        self.visit_times[cip] = times + 1
        print('%s visit %s times'%(cip,self.visit_times[cip]))