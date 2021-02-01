from django.urls import path
from . import views
urlpatterns = [
    #http://127.0.0.1:8000/user/detail/1
    path('detail/<int:uid>',views.user_detail),
    path('update/<int:uid>',views.user_update),

]