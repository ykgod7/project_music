from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm


# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'music/login.html', {'form': form})  # 응답 데이터 전달
