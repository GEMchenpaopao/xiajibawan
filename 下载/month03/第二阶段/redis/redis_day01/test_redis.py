import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

#通过命令对应的python方法
#byte字节,返回的键的类型都是字符串
print(r.keys("*"))
print(r.exists('lk1'))
r.set('name','aid2010班',1000)
print(r.get('name').decode())
#设置多个字符串的键值,参数使用字典
r.mset({'a':100,'b':200,'c':300})
print(r.mget(['a','b','c']))

#列表类型的操作
