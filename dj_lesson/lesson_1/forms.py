from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband


# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзиклмнопрстуфхцчшщьыъэюя0123456789- "
#     code = "Russian"
#
#
#     def __init__(self, message=None):
#         self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел"
#
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5, label="Заголовок",
                            widget=forms.TextInput(attrs={"class": "form-input"}),
                            # validators=[
                            #     RussianValidator(),
                            # ],
                            error_messages={
                                "min_length": "Слишком короткий заголовок",
                                "required": "Без заголовка нельзя"
                            })
    slug = forms.SlugField(max_length=255, label="Путь", validators=[MinLengthValidator(5, message="Должно быть не менее 5 символов"),
                                                                     MaxLengthValidator(100, message="Длина не должна превышать 100 символов")])
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 50, "rows": 5}), label="Контент")
    is_published = forms.BooleanField(required=False, initial=True, label="Опубликовать")
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Нет категории", label="Категории")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label="Не замужем", label="Муж")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзиклмнопрстуфхцчшщьыъэюя0123456789- "

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("Должны присутствовать только русские символы, дефис и пробел")
