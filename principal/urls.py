from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal,name='principal'),
    path('plogin',views.plogin,name='plogin'),
    path('account',views.account,name='account'),
    path('logout', views.logout, name='logout'),
    path('principal_home',views.principal_home,name='principal_home'),
    path('create_faculty_account', views.create_faculty_account, name='create_faculty_account'),
]