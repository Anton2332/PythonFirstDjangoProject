from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страниці приложения reading")


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




