from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import json
from alipay import AliPay

# 读取秘钥文件获取私钥和支付宝的公钥
app_private_key_string = open(settings.ALIPAY_KEY_DIR + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIR + 'app_public_key.pem').read()


class MyAlipay(View):
    def __init__(self, **kwargs):
        # 首先调用父类的构造函数
        super().__init__(**kwargs)
        # 创建一个Alipay对象
        self.alipay = AliPay(
            # 应用ID
            appid=settings.ALIPAY_APP_ID,
            # 接收支付宝的url
            app_notify_url=None,
            # 用户私钥
            app_private_key_string=app_private_key_string,
            # 支付宝公钥
            alipay_public_key_string=alipay_public_key_string,
            # 非对称加密算法
            sign_type='RSA2',
            # 指定为调试模式请求发送到沙箱服务器
            debug=True

        )

    def get_trade_url(self, order_id, amount):
        base_url = 'https://openapi.alipaydev.com/gateway.do'
        # 根据参数生成订单的查询字符串
        order_string = self.alipay.api_alipay_trade_page_pay(
            # 1 订单编号
            out_trade_no=order_id,
            # 2 订单总金额
            total_amount=amount,
            # 3 订单标题
            subject=order_id,
            # 4 用户支付完成后,告知支付宝跳转到商家的那个页面
            return_url=settings.ALIPAY_RETURN_URL,
            # 5 支付结果通知的url
            notify_url=settings.ALIPAY_NOTIFY_URL,
        )
        return base_url + '?' + order_string


class JumpView(MyAlipay):
    def get(self, request):
        return render(request, 'ajax_alipay.html')

    def post(self, request):
        # 从前端接收订单编号
        json_str = request.body
        json_obj = json.loads(json_str)
        # 取出订单编号
        order_id = json_obj['order_id']
        # 生成并返回一个pay_url
        # 参数1:订单编号   参数2:订单金额
        pay_url = self.get_trade_url(order_id, 999)
        return JsonResponse({'pay_url': pay_url})

ORDER_STATUS = 1

class ResultView(MyAlipay):
    def get(self,request):
       # return HttpResponse('支付过程完成,跳转到该页面!')
        request_data = {k: request.GET[k] for k in request.GET.keys()}
        # 从request_data 获取订单编号
        order_id = request_data['out_trade_no']
        #到底需不需要主动查询?
        #如果支付过程完成了,但是数据库中的订单状态仍然是未支付状态
        if ORDER_STATUS ==1:
            #需要主动查询
            request = self.alipay.api_alipay_trade_query(out_trade_no=order_id)
            if request.get('trade_status')=='TRADE_SUCCESS':
                # 修改数据库的订单状态,将来支付修改为支付成功!
                return HttpResponse('主动查询结果是:支付成功!')
            else:
                # 修改数据库的订单状态,将来支付修改为支付失败!
                return HttpResponse('主动查询结果是:支付失败!')
        elif ORDER_STATUS==2:
            return HttpResponse('支付成功!')
        elif ORDER_STATUS==3:
            return HttpResponse('支付失败!')




    # 可能还有另外一个有IP地址的服务器,接收支付发送的post请求
    #告知其支付结果
    def post(self,request):
        # 1 将request.POST这个类字典结构转换为字典结构
        request_data = {k:request.POST[k] for k in request.POST.keys()}
        # 2 从POST中取出支付宝的签名
        sign = request_data.pop('sign')
        #验证签名
        is_verify = self.alipay.verify(request_data,sign)
        if is_verify:
            # 验签通过
        #从request_data中获取订单的支付状态
            trade_status = request_data['trade_status']
            if trade_status == 'TRADE_SUCCESS':
                # 修改数据库中订单的状态,将来支付修改1 为支付成功2
                return HttpResponse('修改订单状态成功!')
            else:
                # 修改数据库中订单的状态,将来支付修改1 为支付失败3
                return HttpResponse('修改订单成功!')
        else:
            return HttpResponse('验签失败,请求不合法')