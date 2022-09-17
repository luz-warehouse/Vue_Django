"""read URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views
router = SimpleRouter()
router.register('super',views.SuperUser,'super')
router.register('',views.UserView,'login')
router.register('register',views.UserRegisterView,'user_register')
router.register('personal',views.PersonalCenter,'personal')  # 个人中心
router.register('check_pwd',views.ChangePasswordView,'check_pwd')  # 修改密码
router.register('seticon',views.SetIcon,'seticon')  # 修改密码
router.register('setcoin',views.SetCoin,'setcoin')  # 更新屋币


urlpatterns = [
    path('', include(router.urls)),
    path('success/',views.SuccessView.as_view())
]
