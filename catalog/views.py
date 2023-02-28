from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import DetailView
# Create your views here.


class ProductView(DetailView):
    model = Product
    template_name = 'catalog/db_record.html'
    context_object_name = 'record'


def index(request):
    data = {
        'values': ['1', '2', '3',],
        'slovar': {
            'car': 'BMW',
            'age': '18',
        }
    }
    return render(request, 'catalog/index.html', data)

def about(request):
    return render(request, 'catalog/about.html')

def specs(request):
    form = ProductFrom
    data = {
        'form' : form
    }

    product = Product.objects.all()
    return render(request, 'catalog/specs.html', {'data': data})

def workers(request):
    return render(request, 'catalog/workers.html')

def builds(request):
    return render(request, 'catalog/builds.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def db_record(request):
    my_record = Product.objects.all()
    return render(request, 'catalog/db_record.html', {"my_record": my_record})