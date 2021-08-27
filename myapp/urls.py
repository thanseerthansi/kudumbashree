"""kudumbasree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from.import views
from django.urls import path,include

urlpatterns = [
    path('',views.home),
    path('contact/',views.contact),
    path('login/',views.login),
    path('admintable/',views.admintable),
    path('log/',views.log),
    path('about/',views.about),
    path('secretarytable/',views.secretarytable),
    path('admcontact/',views.admcontact),
    path('addmembers/',views.addmembers),
    path('attendence/',views.attendence),
    path('loanapplication/',views.loanapplication),
    path('pro_ajax/',views.ajax),
    path('loandetail/',views.loandetail),
    path('approve/',views.approve),
    path('loantracking/',views.loantracking),
    path('addamount/',views.addamount),
    path('cancel/',views.cancel),
    path('loanstatus/',views.loanstatus),
    path('detail/',views.detail),
    path('att_dis/',views.att_dis),
    path('saddmembers/',views.saddmembers),
    path('sattendence/',views.sattendence),
    path('sloanapplication/',views.sloanapplication),
    path('sloantracking/',views.sloantracking),
    path('saddamount/',views.saddamount),
    path('presidenttable/',views.presidenttable),
    path('paddmembers/',views.paddmembers),
    path('pattendence/',views.pattendence),
    path('ploandetail/',views.ploandetail),
    path('papprove/',views.papprove),
    path('pcancel/',views.pcancel),
    path('ploanstatus/',views.ploanstatus),
    path('pdetail/',views.pdetail),
    path('emajax/',views.emajax),

    
]
