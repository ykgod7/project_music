from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from music.models import Profile
from .forms import UserForm, PopupLoginForm
import json
import logging

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Profile.objects.create(user=request.user)
            return redirect(request.POST.get('next') or 'index')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})


def popuplogin(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect(request.POST.get('next'))
        # else:
        #     form = PopupLoginForm(request=request)
        #     form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
        # return HttpResponse({'form': form})
        form = PopupLoginForm(request=request, data=request.POST)
        if form.is_valid():

            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            # return redirect(request.POST.get('next'))
            return HttpResponse(json.dumps({'result': 'true'}), content_type='application/json')
        else:
            context = {}
            return HttpResponse(json.dumps({'result': 'false', 'con': form.errors}), content_type='application/json')

