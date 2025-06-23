from django.contrib import admin
from .models import LessonForDB, Category


@admin.register(LessonForDB)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    ordering = ['time_create']
    list_editable = ('is_published', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')