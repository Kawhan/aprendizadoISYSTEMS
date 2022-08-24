from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.listarProdutos, name='produtos'),
    path('categoria', views.listarCategoria, name='categoria')
]
