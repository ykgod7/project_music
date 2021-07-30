from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm


# Create your views here.
def login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        # 정상적인 데이터인지 확인
        if form.is_valid():
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'music/login.html', {'form': form})  # 응답 데이터 전달
