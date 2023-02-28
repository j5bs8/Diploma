from .models import *
from django.forms import ModelForm


class ProductFrom(ModelForm):
    class Meta:
        model = Product
        fields = ['model', 'model', 'form_factor', 'cpu', 'memory', 'pci', 'back_panel', 'audio', 'network', 'image' ]