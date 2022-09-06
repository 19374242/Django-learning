# publish/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),  # 指定register函数的路由为register
    path('login', login),
    path('change_password', change_password),
    path('del_account', del_account),
    path('show_account', show_account),
    path('show_one_account', show_one_account),
    path('show_some_account', show_some_account)
]