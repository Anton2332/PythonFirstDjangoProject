from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories)#страндартна маршрутизація
    ,
    re_path(r'archive/(?P<year>[0-9]{4})/', archive)#спіцифічний маршрут з органіченіям на 4 цифри
]