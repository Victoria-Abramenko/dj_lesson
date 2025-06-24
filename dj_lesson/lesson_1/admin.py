from django.contrib import admin, messages
from .models import LessonForDB, Category


@admin.register(LessonForDB)
class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', "show_info")
    list_display_links = ('title', )
    ordering = ['time_create']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']

    @admin.display(description="Краткое описание", ordering='content')
    def show_info(self, obj_lesson = LessonForDB):
        return f" Описание {len(obj_lesson.content)} символов"


    @admin.action(description="Опубликовать статью")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=LessonForDB.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")


    @admin.action(description="Снять статью спубликации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=LessonForDB.Status.DRAFT)
        self.message_user(request, f"Изменено {count} записей", messages.Warning)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')