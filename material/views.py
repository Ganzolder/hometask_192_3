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
from django.urls import reverse_lazy, reverse
from material.models import Material
from pytils.translit import slugify
from django.shortcuts import get_object_or_404, redirect


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('material:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)




class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('material:list')


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('material:view', args=[self.kwargs.get('pk')])

class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('material:list')


def toggle_activity(request, pk):
    material_item = get_object_or_404(Material, pk=pk)
    if material_item.is_published:
        material_item.is_published = False
    else:
        material_item.is_published = True

    material_item.save()

    return redirect(reverse('material:list'))
