from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.articleslist, name='list'),
    path('<slug>', views.article_detail, name='detail')

]
