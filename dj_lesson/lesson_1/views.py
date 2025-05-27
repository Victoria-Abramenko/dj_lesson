from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'биография Джулии Робертс', 'is_published': True}
]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


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
        # return redirect('/')
        # return redirect('/', permanent=True)
        # return redirect(index)
        # return redirect('home_page')
        # return redirect('other_slug_page','music')
        ur = reverse('other', args=('music', ))
        # return redirect(ur)
        return HttpResponseRedirect(ur)

    return HttpResponse(f'<h1>Отображение страницы по запросу other </h1><p>архив: {year}</p>')

def func_page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
