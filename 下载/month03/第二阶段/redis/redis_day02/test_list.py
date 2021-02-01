import redis
r = redis.Redis(password='123456')
if __name__ == '__main__':
    print(r.keys('*'))
    r.flushdb()
    #操作列表
    r.rpush('spider:urls','01_baidu.com','02_taobao.com','03_sina.com','04_jd.com','05_xxx.com')
    #查看列表中所有元素
    print(r.lrange('spider:urls', 0, -1))
    #查看列表长度
    print(r.llen('spider:urls'))
    #将列表中01_baidu.com 改为 01_tmall.com
    print(r.lset('spider:urls', 0, '01_tmall.com'))
    #尾部弹出
    print(r.rpop('spider:urls'))
    #删除列表元素
    print(r.lrem('spider:urls', 0, '02_taobao.com'))
    #剔除列表中的其他元素，只剩前3条
    print(r.ltrim('spider:urls', 0, 2))
    print(r.keys('*'))
    print(r.lrange('spider:urls', 0, -1))

