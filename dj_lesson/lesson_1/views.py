from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Отображение стартовой страницы домену')

def next_page(request):
    return HttpResponse('Отображение страницы по запросу lesson_1')

def other_page(request):
    return HttpResponse('<h1>Отображение страницы по запросу other</h1>')