"""attendance URL Configuration"""
from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_header = "Attendance System"
admin.site.site_title = "Attendance System"
admin.site.index_title = "Attendance Site"

urlpatterns = [
    path('', views.index,name='index'),
    path('faculty/', include('faculty.urls')),
    path('student/', include('student.urls')),
    path('admin/', admin.site.urls),
]
