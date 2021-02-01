import redis
r = redis.Redis(password='123456')

r.flushdb()
# 操作hash
r.hset('pyhk1','name','aid2010')
print(r.hget('pyhk1', 'name'))
r.hmset('pyhk1',{'age':18,'city':'杭州'})
print(r.hgetall('pyhk1'))
print(r.hget('pyhk1','city').decode())
print(r.hvals('pyhk1'))
print(r.hkeys('pyhk1'))