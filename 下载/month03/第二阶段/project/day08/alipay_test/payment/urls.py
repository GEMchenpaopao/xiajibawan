from django.urls import path
from payment import views
urlpatterns = [
    path('jump/',views.JumpView.as_view()),
    path('result/',views.ResultView.as_view()),
]