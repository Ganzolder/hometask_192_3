from django.http import HttpRequest
from django.conf import settings

def page_type(request):
    if '/category_catalog/' in request.path:
        page_type = 'catalog'
    else:
        page_type = 'product'

    return {'page_type': page_type}