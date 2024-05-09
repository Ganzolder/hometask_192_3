from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import MainConfig
from catalog.views import IndexListView, ContactTemplateView, ProductsListView, ProductDetailView, CategoryListView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, ProductCategoryUpdateView, ProductDescriptionUpdateView, \
    ProductPublishUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index_list'),
    path('contacts_template/', ContactTemplateView.as_view(), name='contacts_template'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('products_list/<int:pk>/', ProductsListView.as_view(), name='products_list'),
    path('product_page/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_page'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('edit/<int:pk>/category', ProductCategoryUpdateView.as_view(), name='edit_category'),
    path('edit/<int:pk>/description', ProductDescriptionUpdateView.as_view(), name='edit_description'),
    path('edit/<int:pk>/publish', ProductPublishUpdateView.as_view(), name='edit_publish'),



]
