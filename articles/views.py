from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.

def articleslist(request):
    articles = models.Articles.objects.all()
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)


def article_detail(request, slug):
    return HttpResponse(slug)
