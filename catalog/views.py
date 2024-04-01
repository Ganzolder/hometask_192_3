from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

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
        'title' : f'Yoni products catalogue {category_item}'
    }
    return render(request, 'catalog/products_catalog.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title' : 'Категории товаров'
    }

def product_page(request, pk):

    context = {
        'product_page': Product.objects.get(pk=pk),
        'product_info' : Product.objects.filter(pk=pk),
        'title': 'Yoni product page'
    }
    return render(request, 'catalog/product_page.html', context)

