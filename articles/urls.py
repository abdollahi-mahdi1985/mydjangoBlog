from django.urls import path
from . import views

urlpatterns = [
    path('', views.articleslist, name='articles'),

]
