from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import AddPostForm, UploadFileForm
from .models import LessonForDB, Category, TagPosts, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


# def index(request):
#     posts = LessonForDB.published.all().select_related("cat")
#     data = {'title': 'Главная страница сайта',
#             'text': '',
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': 0}
#     return render(request, 'lesson_temp/index.html', context=data)


# class HomePage(TemplateView):
#     template_name = 'lesson_temp/index.html'
#     extra_context = {
#         'title': 'Главная страница сайта',
#         'text': '',
#         'menu': menu,
#         'posts': LessonForDB.published.all().select_related("cat"),
#         'cat_selected': 0
#     }


class HomePage(ListView):
    # model = LessonForDB
    template_name = 'lesson_temp/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница сайта',
        'text': '',
        'menu': menu,
        'cat_selected': 0
    }


    def get_queryset(self):
        return LessonForDB.published.all().select_related("cat")


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница сайта'
    #     context['menu'] = menu
    #     context['posts'] =  LessonForDB.published.all().select_related("cat")
    #     context['cat_selected'] = int(self.request.GET.get('cat_id, 0'))
    #     return context


# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data["file"])
            fp = UploadFiles(file=form.cleaned_data["file"])
            fp.save()
    else:
        form = UploadFileForm()

    return render(request, 'lesson_temp/about.html', {'title': 'О сайте', 'menu': menu, 'form': form})


#
# def show_post(request, post_slug):
#     post = get_object_or_404(LessonForDB, slug=post_slug)
#     data = {
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': 1,
#     }
#
#     return render(request, 'lesson_temp/post.html', data)


class ShowPost(DetailView):
    model = LessonForDB
    template_name = 'lesson_temp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context


    def get_object(self, queryset=None):
        return get_object_or_404(LessonForDB.published, slug=self.kwargs[self.slug_url_kwarg])



# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # try:
#             #     LessonForDB.objects.create(**form.cleaned_data)
#             # except:
#             #     form.add_error(None, "Ошибка при добавлении поста")
#             #     return redirect("home_page")
#             form.save()
#             return redirect("home_page")
#     else:
#         form = AddPostForm()
#
#     data = {
#         "menu": menu,
#         "title": "Добавление статьи",
#         "form": form
#     }
#     return render(request, 'lesson_temp/addpage.html', data)


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            "menu": menu,
            "title": "Добавление статьи",
            "form": form
        }
        return render(request, 'lesson_temp/addpage.html', data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home_page")

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


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = LessonForDB.published.filter(cat_id=category.pk).select_related("cat")
#     data = {'title': f'Рубрика: {category.name}',
#             'text': '',
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': category.pk}
#     return render(request, 'lesson_temp/index.html', context=data)


class ShowCategory(ListView):
    template_name = 'lesson_temp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    
    def get_queryset(self):
        return LessonForDB.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория - ' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context



# def show_tag_posts_list(request, tag_slug):
#     tag = get_object_or_404(TagPosts, slug=tag_slug)
#     posts = tag.tags.filter(is_published=LessonForDB.Status.PUBLISHED).select_related("cat")
#
#     data = {
#         'title': f"Тег: {tag.tag}",
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': None,
#     }
#
#     return render(request, 'lesson_temp/index.html', context=data)


class TagPostList(ListView):
    template_name = 'lesson_temp/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPosts.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context

    def get_queryset(self):
        return LessonForDB.published.filter(tags__slug=self.kwargs['tag_slug']).select_related("cat")


def func_page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")