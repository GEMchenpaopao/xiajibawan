import redis
r = redis.Redis(password='123456')

r.flushdb()

# 有序集合的操作
r.zadd('zk1',{'tedu':100,'tedu2':200})
print(r.zrange('zk1', 0, -1, withscores=True))
r.zadd('zk2',{'tedu':100,'tedu3':200})
print(r.zrange('zk2', 0, -1, withscores=True))

print(r.zunionstore('zk3', ['zk1', 'zk2'], aggregate='sum'))
print(r.zrange('zk3', 0, -1, withscores=True))
print(r.zunionstore('zk4', {'zk1': 0.8, 'zk2': 0.2}, aggregate='sum'))
print(r.zrange('zk4',0,-1,withscores=True))