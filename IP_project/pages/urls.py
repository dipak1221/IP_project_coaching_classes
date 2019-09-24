

from django.urls import path
from . import views

urlpatterns = [

    path('index/',views.index,name='index'),
    path('notice/',views.notice,name='notice'),
    path('add_notice/',views.add_notice,name='add_notice'),
    path('login/',views.login,name='login'),
    path('verify_login/',views.verify_login,name='verify_login'),
    path('expand_notice/',views.expand_notice,name='expand_notice'),
    path('list_notice/',views.list_notice,name='list_notice'),
    #path('modify_notice/',views.modify_notice,name='modify_notice'),


]
