from .login_dec import get_user_by_request
from django.core.cache import cache
def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request,*args,**kwargs):
            # 具体的缓存实现
            if 't_id' in request.GET.keys():
                return func(request,*args,**kwargs)

            #是否是博主访问自己
            #访问者的名称
            visitor_name = get_user_by_request(request)
            author_name = kwargs['author_id']

            if visitor_name == author_name:
                #博主访问自己
                cache_key= 'topic_cache_self_%s'%(request.get_full_path())
            else:
                cache_key = 'topic_cache_%s' % (request.get_full_path())
            print('-----cache_key is %s----'%cache_key)
            #缓存思想,有缓存访问缓存,没有缓存调用视图函数
            res = cache.get(cache_key)
            if res:
                print('----cache in----')
                return res
            res = func(request,*args,**kwargs)
            cache.set(cache_key,res,expire)
            return res

        return wrapper
    return _topic_cache