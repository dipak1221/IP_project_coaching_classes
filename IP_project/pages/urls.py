

from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('notice/',views.notice,name='notice'),
    path('login/',views.login,name='login'),
    path('verify_login',views.verify_login,name='verify_login'),


]
