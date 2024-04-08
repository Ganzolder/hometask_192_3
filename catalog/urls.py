from django.urls import path
from catalog.apps import MainConfig
from catalog.views import IndexListView, ContactTemplateView, ProductsListView, ProductDetailView, CategoryListView


app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index_list'),
    path('contacts_template/', ContactTemplateView.as_view(), name='contacts_template'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('products_list/<int:pk>/', ProductsListView.as_view(), name='products_list'),
    path('product_page/<int:pk>/', ProductDetailView.as_view(), name='product_page'),

]
