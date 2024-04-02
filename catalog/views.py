from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView

# Create your views here.
def index(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Главная',
    }
    return render(request, 'catalog/index.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}, {email}')
    return render(request, 'catalog/contacts.html')

def products_catalog(request, pk):

    category_item = Category.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title' : f'Товары категории {category_item}'
    }
    return render(request, 'catalog/products_catalog.html', context)


def category_list(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров',
    }
    return render(request, 'catalog/category_list.html', context)

def product_page(request, pk):
    product_item = Product.objects.get(pk=pk)
    category_item = Category.objects.get(pk=pk)
    context = {
        'product_page': Product.objects.get(pk=pk),
        'product_info' : Product.objects.filter(pk=pk),
        'title': f'{category_item.name} {product_item.name}'
    }
    return render(request, 'catalog/product_page.html', context)

