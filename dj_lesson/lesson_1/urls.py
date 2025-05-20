from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('lesson_1/', views.next_page),
    path('other/', views.other_page),
]