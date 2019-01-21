import random

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render


from django.urls import reverse

from user.models import User, UserToken


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = User.objects.filter(username=username).first()
        if check_password(password, user.password):
            # 1.向cookie中保存键值对，键为sessionid
            # 2.向django_session表中存sessionid值
            # 3.向django_session表中存键值对{'username':'xxx'}
            print('pass')
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('app:index'))
        else:
            print('i')
            return render(request, 'login.html')


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).first():
            msg = '账号已存在'
            return render(request, 'register.html', {'msg': msg})
        if password1 != password2:
            msg1 = '密码不一致'
            return render(request, 'register.html', {'msg1': msg1})
        password = make_password(password1)
        User.objects.create(username=username, password=password)
        return HttpResponseRedirect(reverse('user:login'))


# 注销
def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('user:login'))








