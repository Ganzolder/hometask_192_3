import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Versions
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from config import settings
from users.models import User


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

        #category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        product = self.get_object()
        category = product.category
        context_data['category_pk'] = category.pk

        context_data['title'] = f'Товары категории {category}'

        return context_data


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)

class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionsFormset = inlineformset_factory(Product, Versions, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionsFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionsFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]

        if formset.is_valid():
            self.object = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.product = self.object  # Установка связи с продуктом
                instance.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:category_list")

    import secrets
    from django.contrib.auth.models import User
    from django.contrib.auth.hashers import make_password
    from django.core.mail import send_mail
    from django.shortcuts import render
    from django.views import View




