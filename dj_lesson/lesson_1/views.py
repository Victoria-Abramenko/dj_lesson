from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddPostForm, UploadFileForm
from .models import LessonForDB, Category, TagPosts, UploadFiles
from .utils import DataMixin


class HomePage(DataMixin, ListView):
    template_name = 'lesson_temp/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница сайта'
    cat_selected = 0

    def get_queryset(self):
        return LessonForDB.published.all().select_related("cat")

def about(request):
    contact_list = LessonForDB.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.Get.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'lesson_temp/about.html', {'title': 'О сайте', 'page_obj': page_obj})


class ShowPost(DataMixin, DetailView):
    template_name = 'lesson_temp/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(LessonForDB.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'lesson_temp/addpage.html'
    title_page = 'Добавление статьи'


class UpdatePage(DataMixin, UpdateView):
    model = LessonForDB
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'lesson_temp/addpage.html'
    success_url = reverse_lazy('home_page')
    title_page = 'Добавление статьи'

def contact(request):
    return HttpResponse(f"Страница с контактами")

def login(request):
    return HttpResponse(f"Авторизация")


class ShowCategory(DataMixin, ListView):
    template_name = 'lesson_temp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    
    def get_queryset(self):
        return LessonForDB.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title='Категория - ' + cat.name, cat_selected=cat.pk)


class TagPostList(DataMixin, ListView):
    template_name = 'lesson_temp/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPosts.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Тег: ' + tag.tag)

    def get_queryset(self):
        return LessonForDB.published.filter(tags__slug=self.kwargs['tag_slug']).select_related("cat")


def func_page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")