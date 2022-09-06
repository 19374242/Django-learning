import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from login.models import User


# 注册
@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'GET':  # POST也一样
        username = request.GET.get('username')  # 获取请求体中的请求数据
        password = request.GET.get('password')
        # get如果不存在会报错,多于一个数据会报错
        user = User.objects.filter(name=username)
        # 不能用none
        if len(user) == 0:
            User.objects.create(name=username, password=password)
            return JsonResponse({'errno': 0, 'msg': "注册成功"})
        else:
            return JsonResponse({'errno': 1, 'msg': "用户已存在"})
    else:
        return JsonResponse({'errno': 2, 'msg': "应使用get方法"})


# 登录
@csrf_exempt  # 跨域设置
def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = User.objects.filter(name=username)
        # 不能用none,user是个数组
        if len(user) == 0:
            return JsonResponse({'errno': 1, 'msg': "用户不存在"})
        else:
            if user[0].password != password:
                return JsonResponse({'errno': 2, 'msg': "密码错误"})
            else:
                return JsonResponse({'errno': 0, 'msg': "登录成功"})
    else:
        return JsonResponse({'errno': 3, 'msg': "应使用get方法"})


# 修改密码
@csrf_exempt  # 跨域设置
def change_password(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = User.objects.filter(name=username)
        # 不能用none,user是个数组
        if len(user) == 0:
            return JsonResponse({'errno': 1, 'msg': "用户不存在"})
        else:
            user.update(password=password)
            return JsonResponse({'errno': 0, 'msg': "修改密码成功"})
    else:
        return JsonResponse({'errno': 3, 'msg': "应使用get方法"})


# 注销账号
@csrf_exempt  # 跨域设置
def del_account(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = User.objects.filter(name=username)
        # 不能用none,user是个数组
        if len(user) == 0:
            return JsonResponse({'errno': 1, 'msg': "用户不存在"})
        else:
            user.delete()
            return JsonResponse({'errno': 0, 'msg': "注销成功"})
    else:
        return JsonResponse({'errno': 3, 'msg': "应使用get方法"})


# 显示所有账号
@csrf_exempt  # 跨域设置
def show_account(request):
    if request.method == 'GET':
        user = User.objects.filter()
        data = []
        # 转化为json格式
        if user:
            for i in user:
                data.append(model_to_dict(i))  # 在data后增加一个对象
        return JsonResponse({'errno': 0, 'msg': "查询成功", 'data': data})
    else:
        return JsonResponse({'errno': 1, 'msg': "应使用get方法"})


# 显示某个账号
@csrf_exempt  # 跨域设置
def show_one_account(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user = User.objects.filter(name=username)
        data = []
        # 转化为json格式
        if user:
            for i in user:
                data.append(model_to_dict(i))  # 在data后增加一个对象
        return JsonResponse({'errno': 0, 'msg': "查询成功", 'data': data})
    else:
        return JsonResponse({'errno': 1, 'msg': "应使用get方法"})

# 显示带有某个字的账号
@csrf_exempt  # 跨域设置
def show_some_account(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        # 模糊查询，注意有两个杠
        user = User.objects.filter(name__contains=username)
        data = []
        # 转化为json格式
        if user:
            for i in user:
                data.append(model_to_dict(i))  # 在data后增加一个对象
        return JsonResponse({'errno': 0, 'msg': "查询成功", 'data': data})
    else:
        return JsonResponse({'errno': 1, 'msg': "应使用get方法"})
