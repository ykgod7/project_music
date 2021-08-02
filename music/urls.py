from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('<str:username>', views.mypage, name='mypage')
]