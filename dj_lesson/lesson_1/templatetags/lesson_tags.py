from django import template
import lesson_1.views as views
from lesson_1.models import Category

register = template.Library()


@register.inclusion_tag('lesson_temp/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}