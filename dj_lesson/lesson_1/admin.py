from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import LessonForDB, Category

class MarriedFilter(admin.SimpleListFilter):
    title = "Статус женщин"
    parameter_name = "status"


    def lookups(self, request, model_admin):
        return [
            ("married", "Замужем"),
            ("single", "Не замужем"),
        ]


    def queryset(self, request, queryset):
        if self.value() == "married":
            return queryset.filter(husband__isnull = False)
        elif self.value() == "single":
            return queryset.filter(husband__isnull = True)


@admin.register(LessonForDB)
class AppAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'slug', 'photo', 'post_photo', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['post_photo']
    prepopulated_fields = {"slug": ("title", )}
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title', )
    filter_horizontal = ['tags']
    ordering = ['time_create']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description="Фотография", ordering='content')
    def post_photo(self, obj_lesson = LessonForDB):
        if obj_lesson.photo:
            return mark_safe(f"<img src='{obj_lesson.photo.url}' width=50>")
        else:
            return "без фото"


    @admin.action(description="Опубликовать статью")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=LessonForDB.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")


    @admin.action(description="Снять статью спубликации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=LessonForDB.Status.DRAFT)
        self.message_user(request, f"Изменено {count} записей", messages.WARNING)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')