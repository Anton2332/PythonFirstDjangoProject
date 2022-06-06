from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories),  # страндартна маршрутизація
    #  re_path(r'archive/(?P<year>[0-9]{4})/', archive, name='archive'),  # спіцифічний маршрут з органіченіям на 4 цифри
    path('about', about, name='about'),
    path('addpag/', addpage, name="add_page"),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
]
