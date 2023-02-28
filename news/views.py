from django.shortcuts import render
from .models import Articles
# Create your views here.

def news_home(request):
    article = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news':article})