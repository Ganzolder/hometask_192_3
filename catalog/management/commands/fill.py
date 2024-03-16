from django.core.management import BaseCommand
from catalog.models import Category, Product
import json
import catalog

class Command(BaseCommand):

    @staticmethod
    def json_read_category():
        with open('category.json', 'r') as file:
            category_data = json.load(file)
        return category_data

    @staticmethod
    def json_read_product():
        with open('product.json', 'r') as file:
            product_data = json.load(file)
        return product_data

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()
        # Удалите все категории

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте

        for category in Command.json_read_category():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'], pk=category['pk'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_product():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        category=Category.objects.get(pk=product['pk']),
                        description=product['fields']['description'],
                        preview=product['fields']['preview'],
                        pk=product['pk'],
                        price_per_unit=product['fields']['price_per_unit'])
            )

        Product.objects.bulk_create(product_for_create)