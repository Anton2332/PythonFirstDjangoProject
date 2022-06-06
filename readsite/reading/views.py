from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'Про сайт', 'url_name': 'about'},
    {'title': "Додати", 'url_name': 'add_page'},
    {'title': 'Зворотній звязок', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name':'login'}
]


def index(request):
    # return HttpResponse("Страниці приложения reading")
    posts = Reader.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Головна сторінка'
    }
    return render(request, 'reading/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'Про сайт'
    }
    return render(request, 'reading/about.html', context=context)


def addpage(request):
    return HttpResponse('Додати статю')


def contact(request):
    return HttpResponse('Зворотній звязок')


def login(request):
    return HttpResponse('Авторизація')


def show_post(request, post_id):
    return HttpResponse(f'ID = {post_id}')


def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Твори по категоріям</h1><p>{catid}</p>")


def archive(request, year):
    # if int(year) > 2020:
    #     raise Http404()

    if int(year) > 2020:
        return redirect('home', permanent=True)  # if permanent True постійний редірект False времений

    return HttpResponse(f"Hello {year} world")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страниці не найдена</h1>')




