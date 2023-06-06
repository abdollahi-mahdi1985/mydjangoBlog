from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required


# Create your views here.

def articleslist(request):
    articles = models.Articles.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)


def article_detail(request, slug):
    article = models.Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login")
def create_article(request):
    return render(request, 'articles/create_atricle.html')
