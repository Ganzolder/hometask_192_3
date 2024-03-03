from django.urls import path
from catalog.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts.html', contacts, name='contacts'),
    path('index.html', index)
]