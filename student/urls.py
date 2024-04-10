"""student URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student,name='student'),
    path('slogin', views.slogin,name='slogin'),
    path('shome', views.shome,name='shome'),
    path('slogout', views.slogout,name='slogout'),
    path('s_chk_att', views.s_chk_att,name='s_chk_att'),
    path('chk_present', views.chk_present,name='chk_present'),
]
