from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.YearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='home_page'),
    path('lesson_1/', views.next_page, name='lesson_page'),
    path('other/<int:other_id>/', views.other_page, name='other_number_page'),
    path('other/<slug:other_slug>/', views.other_by_slug, name='other_slug_page'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.other_archive)
    path('archive/<year4:year>/', views.other_archive, name='archive_page')

]