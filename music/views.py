from django.shortcuts import render
from django.contrib.auth import get_user_model


def mypage(request, username):
    user = get_user_model()
    return render(request, 'mypage.html', {'user': user})


