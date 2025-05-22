from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

def index(request):
    return HttpResponse('Отображение стартовой страницы домену')


def next_page(request):
    return HttpResponse('Отображение страницы по запросу lesson_1')


def other_page(request, other_id):
    return HttpResponse(f'<h1>Отображение страницы по запросу other</h1><p>id: {other_id}</p>')


def other_by_slug(request, other_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Отображение страницы по запросу other со слагом</h1><p>id: {other_slug}</p>')


def other_archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f'<h1>Отображение страницы по запросу other </h1><p>архив: {year}</p>')

def func_page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
