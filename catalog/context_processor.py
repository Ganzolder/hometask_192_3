from django.http import HttpRequest
from django.conf import settings

def page_type(request):
    if 'products_catalog' in request.path:
        page_type = 'products_catalog'
    else:
        page_type = 'catalog'

    return {'page_type': page_type}