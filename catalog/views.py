from django.shortcuts import render
from catalog.models import Category, Product

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}, {email}')
    return render(request, 'main/contacts.html')

def products_catalog(request, pk):

    category_item = Category.objects.get(pk=pk)

    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title' : f'Yoni products catalogue {category_item}'
    }
    return render(request, 'main/products_catalog.html', context)

def category_catalog(request):
    context = {
        'object_list': Category.objects.all(),
        'title' : 'Yoni category catalogue'
    }
    return render(request, 'main/category_catalog.html', context)


def product_page(request, pk):

    context = {
        'product_page': Product.objects.get(pk=pk),
        'title': 'Yoni product page'
    }
    return render(request, 'main/product_page.html', context)

