from django.urls import path
from catalog.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts/', contacts, name='contacts'),
    #path('index.html', index)
]