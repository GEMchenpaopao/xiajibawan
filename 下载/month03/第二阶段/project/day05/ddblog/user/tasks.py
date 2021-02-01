from ddblog.celery import app
from tools.sms import YunTongXin

@app.task
def send_sms(phone,code):
    aid = '8aaf0708773733a8017741b6f90404f5'
    atoken = '4a32b9582769496aa7f089c8bbdf8c03'
    appid = '8aaf0708773733a8017741b6f9d404fb'
    tid = '1'
    #下面是同步方式
    # 1 创建云短信对象
    x = YunTongXin(aid, atoken, appid, tid)
    # 2 发送短信
    res = x.run(phone, code)
    print(res)
