import redis

r = redis.Redis(password='123456')

r.sadd('武将','赵云','马超','周瑜','张飞')
r.sadd('文臣','周瑜','诸葛亮','司马懿','郭嘉')

only_fight = r.sdiff('武将','文臣')
for i in only_fight:
    print(i.decode())
only_study = r.sdiff('文臣','武将')
both = r.sinter('文臣','武将')
one = r.sunion('文臣','武将')

