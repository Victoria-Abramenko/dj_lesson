from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'биография Джулии Робертс', 'is_published': True}
]



def index(request):
    # index_page = render_to_string('lesson_temp/index.html')
    # return HttpResponse(index_page)
    data = {'title': 'Главная страница сайта',
            'text': '',
            'menu': menu,
            'posts': data_db}
    return render(request, 'lesson_temp/index.html', context=data)


def about(request):
    return render(request, 'lesson_temp/about.html', {'title': 'О сайте'})



def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def add_page(request):
    return HttpResponse(f"Добавление статьи")


def contact(request):
    return HttpResponse(f"Страница с контактами")


def login(request):
    return HttpResponse(f"Авторизация")


def func_page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")