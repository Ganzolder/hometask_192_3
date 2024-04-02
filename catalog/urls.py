from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, products_catalog, product_page, category_list


app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category_list/', category_list, name='category_list'),
    path('products_catalog/<int:pk>/', products_catalog, name='products_catalog'),
    path('product_page/<int:pk>/', product_page, name='product_page'),

]
