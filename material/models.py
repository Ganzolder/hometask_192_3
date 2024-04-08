from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='material/', **NULLABLE, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
