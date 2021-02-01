


import time

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(100)
def test_cache(request):
    t1 = time.time()
    time.sleep(3)
    return HttpResponse('time is %s'%t1)

def test_mw(request):

    print('my view in')
    return HttpResponse('my middlware view!')

def test_csrf(request):
    if request.method == 'GET':
        return render(request,'test_crsf.html')
    elif request.method == 'POST':
        username = request.POST['username']
        return HttpResponse('username is %s'%username)