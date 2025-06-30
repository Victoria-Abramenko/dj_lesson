from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from .forms import AddPostForm
from .models import LessonForDB, Category, TagPosts

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = LessonForDB.published.all().select_related("cat")
    data = {'title': 'Главная страница сайта',
            'text': '',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0}
    return render(request, 'lesson_temp/index.html', context=data)


def about(request):
    return render(request, 'lesson_temp/about.html', {'title': 'О сайте', 'menu': menu})



def show_post(request, post_slug):
    post = get_object_or_404(LessonForDB, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'lesson_temp/post.html', data)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                LessonForDB.objects.create(**form.cleaned_data)
            except:
                form.add_error(None, "Ошибка при добавлении поста")
                return redirect("home_page")
    else:
        form = AddPostForm()

    data = {
        "menu": menu,
        "title": "Добавление статьи",
        "form": form
    }
    return render(request, 'lesson_temp/addpage.html', data)


def contact(request):
    return HttpResponse(f"Страница с контактами")


def login(request):
    return HttpResponse(f"Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = LessonForDB.published.filter(cat_id=category.pk).select_related("cat")
    data = {'title': f'Рубрика: {category.name}',
            'text': '',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk}
    return render(request, 'lesson_temp/index.html', context=data)

def show_tag_posts_list(request, tag_slug):
    tag = get_object_or_404(TagPosts, slug=tag_slug)
    posts = tag.tags.filter(is_published=LessonForDB.Status.PUBLISHED).select_related("cat")

    data = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'lesson_temp/index.html', context=data)


def func_page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")