from django.db import models
from django.urls import reverse


class Attractions(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name= 'Текст поста')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name= 'Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name= 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name= 'Время изменения')
    is_published = models.BooleanField(default=True, verbose_name= 'Публикация')
    cat = models.ForeignKey('Category', on_delete= models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

class Meta:
    verbose_name = 'Винодельни Молдовы'
    verbose_name_plural = 'Винодельни Молдовы'
    ordering = ['time_create', 'name']

