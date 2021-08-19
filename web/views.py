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
        Job_main = models.Job_Log_Main.objects.all()
        Job_secondly = models.Job_Log_Secondly.objects.all()
        Job_next = models.Job_Log_Next.objects.all()
    return render(request,'index.html',{'User_name':Account,'Job_main':Job_main,'Job_next':Job_next,'Job_secondly':Job_secondly,'Getuserid':status})

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

def userinfo(request):
    status = request.COOKIES.get('user')
    if not status:
        return redirect('/in/')
    else:
        Getuserid = request.GET.get('userid')
        User_account = models.Job_Account.objects.values().filter(User_account=Getuserid)
        return render(request,'userinfo.html',{'Getuserid':Getuserid,'User_account':User_account})

def edit_user(request):
    if request.method == 'GET':
        return render(request,'edit_user.html')
    status = request.COOKIES.get('user')
    if not status:
        return redirect('/in/')
    Getuser_name = request.POST.get('user_name')
    Getuser_number = request.POST.get('user_number')
    Getuser_post = request.POST.get('user_post')
    change = models.Job_Account.objects.get(User_account=status)
    change.User_name = Getuser_name
    change.User_number = Getuser_number
    change.User_post = Getuser_post
    change.save()
    return render(request,'edit_user.html')

def main_log(request):
    status = request.COOKIES.get('user')
    if not status:
        return redirect('/in/')
    else:
        loginfo = models.Job_Log_Main.objects.all()
        lenth = len(loginfo)
        i = 0
        getinfo = []
        for i in range(lenth):
            getinfo.append(loginfo[i])
            userinfo = models.Job_Account.objects.get(User_account=getinfo[i].Main_useraccount)
            getinfo[i].Main_username = userinfo.User_name
            i += i
        loginfo = getinfo
        print(getinfo[0].Main_username)
        return render(request,'main_log.html',{'loginfo':loginfo})

















