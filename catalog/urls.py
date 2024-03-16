from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts, products_catalog, product_page, category_catalog


app_name = MainConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/products_catalog/', products_catalog, name='products_catalog'),
    path('product_page/', product_page, name='product_page'),
    path('category_catalog/', category_catalog, name='category_catalog'),

]
