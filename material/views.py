'''from django.shortcuts import render'''

# Create your views here.
'''class BlogTemplateView(TemplateView):
    model = Product
    template_name = 'catalog/product_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Товары категории {category_item}'

        return context_data'''

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from material.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('material:list')


class MaterialListView(ListView):
    model = Material


class MaterialDetailView(DetailView):
    model = Material


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('material:list')


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('material:list')
