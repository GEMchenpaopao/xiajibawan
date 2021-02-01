"""ddblog URL Configuration

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
from django.urls import path, include
from . import views
from user import views as user_view
from btoken import views as btoken_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_core',views.test_core),
    path('test_core_server',views.test_core_server),
    #博客项目的路由设置
    #CBV
    #as_view()的作用根据请求方法,在视图类中查找对应
    #类的方法,找到后调用即可.找不到
    path('v1/users',user_view.UserView.as_view()),
    path('v1/users/',include('user.urls')),
    path('v1/tokens',btoken_views.TokenView.as_view()),
    path('v1/topics/',include('topic.urls')),
    path('v1/messages/',include('message.urls')),
]
#做静态绑定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)