"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.page_index),
    # http://127.0.0.1:8000/page/2003
    #第三个参数就是给url的值起名称.
    #从语法的角度去理解,相当于pagen这个变量的值是'page/2003'
    path('page/<int:num>',views.page_num),
    path('page/<int:num1>/<str:zifuchuan>/<int:num2>',views.page_zifuchuan),
    path('page/2003',views.page_2003,name='pagen'),
    path('page/2004',views.page_2004),
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.birthday_view),

]
