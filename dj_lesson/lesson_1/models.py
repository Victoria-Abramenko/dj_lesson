from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify
from django.urls import reverse


def translate_to_english(s: str) -> str:
    dic = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
           'г': 'g', 'д': 'd', 'е': 'e','ё': 'e', 'ж': 'zh',
           'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
           'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh',
           'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
           'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'}

    return "".join(map(lambda x: dic[x] if dic.get(x, False) else x, s.lower()))



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=LessonForDB.Status.PUBLISHED)


class LessonForDB(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]),Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категория")
    tags = models.ManyToManyField('TagPosts', blank=True, related_name='tags', verbose_name="Тег")
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True, blank=True, related_name='wife', verbose_name="Муж")

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translate_to_english(self.title))
    #     super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Слаг')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPosts(models.Model):
    tag = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)


    def __str__(self):
        return self.tag


    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

