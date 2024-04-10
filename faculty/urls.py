"""faculty URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty,name='faculty'),
    path('flogin', views.flogin,name='flogin'),
    path('home', views.home,name='home'),
    path('logout', views.logout,name='logout'),
    path('account', views.account,name='account'),
    path('create_account', views.create_account,name='create_account'),
    path('update_att', views.update_att,name='update_att'),
    path('up_attend', views.up_attend,name='up_attend'),
    path('chk_att', views.chk_att,name='chk_att'),
    path('chk_present', views.chk_present,name='chk_present'),
]
