from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}, {email}')
    return render(request, 'main/contacts.html')