from django.shortcuts import render
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView, TemplateView


class IndexListView(ListView):
    model = Category

    def get_queryset(self):
        return super().get_queryset()[:3]

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = f'Главная'

        return context_data


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts_template.html'

    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}, {email}')

        return render(request, 'catalog/contacts.html')


class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Товары категории {category_item}'

        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Товары категории {category_item}'

        return context_data
