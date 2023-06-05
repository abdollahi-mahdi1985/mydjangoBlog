from django.shortcuts import render
from . import models


# Create your views here.

def articleslist(request):
    articles = models.Articles.objects.all()
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)
