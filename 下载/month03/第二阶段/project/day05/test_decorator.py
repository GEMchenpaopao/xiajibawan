import time
def func():
    print('hello')
    time.sleep(1)
    print('world')
#打印该函数执行的时间消耗
def func_ex():
    starttime = time.time()
    print('hello')
    time.sleep(1)
    print('world')
    endtime = time.time()
    timeout = endtime-starttime
    print(timeout)
# 扩展函数功能[不修改原有函数]

def deco3(func):
    def wrapper(a,b):
        startTime=time.time()
        func(a,b)
        endtime = time.time()
        timeout = endtime-startTime
        print(timeout)

    return wrapper
#原始函数
@deco3
def func_param(a,b):
    print('函数的功能是求两个数值的和:')
    time.sleep(1)
    print('result is %s'%(a+b))

#试用装饰器修饰带参数的函数,被修饰的参数个数不定长
def deco4(func):
    def wrapper(*args,**kwargs):
        startTime = time.time()
        func(*args,**kwargs)
        endtime = time.time()
        timeout = endtime-startTime
        print(timeout)
    return wrapper
@deco4
def sum_two(a,b):
    print('求两个数值的和:')
    time.sleep(1)
    print('a+b=%s'%(a+b))
@deco4
def sum_three(a,b,c):
    print('求三个数值的和:')
    time.sleep(1)
    print('a+b+c=%s' % (a + b+c))

def deco_param(expire):
    def _deco_param(func):
        def wrapper():
            starttime = time.time()
            print('expire is %s'%expire)
            func()
            endtime = time.time()
            timeout = endtime-starttime
            print(timeout)
        return wrapper
    return _deco_param
@deco_param(10)
def func3():
    print('hello')
    time.sleep(1)
    print('world')





if __name__ == '__main__':
    func3()