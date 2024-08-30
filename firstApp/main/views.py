from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home Page',
        'values': ['Some', 'Home', '1234'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
