# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render,redirect
import random,hashlib
from web import models
from django.views.decorators import csrf
from django.http import HttpRequest

def login(request):
    if request.COOKIES.get('user'):
        return redirect('/index/')
    if request.method == 'GET':
        return render(request,'in.html')
    username = request.POST.get('user')
    password = request.POST.get('passwd')
    user_obj = models.Job_Account.objects.filter(User_account=username,User_password=password).first()
#    ---------密码加密
#    cookie_random = str(random.random())
#    cookie_md5 = hashlib.md5()
#    cookie_md5.update(cookie_random.encode(encoding='utf-8'))
#    cookie = cookie_md5.hexdigest()
    #   print (user_obj.User_account)
#   ----------
    if not user_obj:
        return render(request,'in.html',{'filed':'用户名或密码有问题。'})
    else:
        rep = redirect('/index/')
        rep.set_cookie('user',username,)
        return rep


def index(request):
#    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('user')
    if not status:
        return redirect('/in/')
    else:
        Account = models.Job_Account.objects.all()
    return render(request,'index.html',{'User_name':Account,'User_number':Account,'User_account':Account,'User_post':Account})

def logout(request):
    rep = redirect('/in/')
    rep.delete_cookie('user')
    return rep

def passwd_change(request):
    if request.method == 'GET':
        return render(request,'passwd_change.html')
    status = request.COOKIES.get('user')
    if not status:
        return redirect('/in/')
    password = request.POST.get('password')
    change = models.Job_Account.objects.get(User_account=status)
    change.User_password = password
    change.save()
    return render(request,'passwd_change.html',{'password_change':'密码修改成功'})

def Log(request,account):
    status = request.COOKIES.get('user')
    if not status:
        return redirect('/in/')
    else:
        job_main = models.Job_Log_Main.objects.filter(Main_useraccount = account)
        job_secondly = models.Job_Log_Secondly.filter(Secoundly_useraccount = account)
        job_next = models.Job_Log_Next.filter(Next_useraccount = account)
        return render(request,'log.html',{'useraccount':job_main})
########
#123342353452345
########















