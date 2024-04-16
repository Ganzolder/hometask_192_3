from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Versions
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')
    #success_url = reverse_lazy('catalog:products_list', args=[self.kwargs.get('pk')])

    '''def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)'''


class ProductUpdateView(UpdateView):
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
        '''context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save'''
        formset = self.get_context_data()["formset"]
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
