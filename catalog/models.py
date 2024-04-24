from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    #objects = None
    name = models.CharField(max_length=250, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'


class Versions(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name=('Продукт'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    version_name = models.CharField(max_length=100, verbose_name=('Название версии'))
    specs = models.TextField(verbose_name='Описание', **NULLABLE)
    version_number = models.CharField(max_length=50, verbose_name=('Номер версии'))
    is_current = models.BooleanField(default=False, verbose_name=('Текущая версия'))
    objects = models.Manager()

    def __str__(self):
        return f'{self.version_name} ({self.product})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
