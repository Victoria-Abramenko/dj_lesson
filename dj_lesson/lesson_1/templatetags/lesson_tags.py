from django import template
from django.db.models import Count

import lesson_1.views as views
from lesson_1.models import Category, TagPosts
from lesson_1.utils import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu


@register.inclusion_tag('lesson_temp/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('lesson_temp/list_tags.html')
def show_all_tags(cat_selected=0):
    return {'tags': TagPosts.objects.annotate(total=Count("tags")).filter(total__gt=0)}