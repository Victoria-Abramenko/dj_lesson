from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Отображение стартовой страницы домену')


def next_page(request):
    return HttpResponse('Отображение страницы по запросу lesson_1')


def other_page(request, other_id):
    return HttpResponse(f'<h1>Отображение страницы по запросу other</h1><p>id: {other_id}</p>')


def other_by_slug(request, other_slug):
    return HttpResponse(f'<h1>Отображение страницы по запросу other со слагом</h1><p>id: {other_slug}</p>')


def other_archive(request, year):
    return HttpResponse(f'<h1>Отображение страницы по запросу other </h1><p>архив: {year}</p>')
