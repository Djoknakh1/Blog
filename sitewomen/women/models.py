from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField(to='Tags', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Comment(MPTTModel):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created_at',)


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
