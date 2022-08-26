from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.listarProdutos, name='produtos'),
    path('categoria', views.listarCategoria, name='categoria'),
    path('<int:produto_id>/view', views.informacao, name='informacao'),
    path('create-produto', views.create_produto, name='create_produto'),
    path('<int:produto_id>/change', views.change_produto, name='change_produto'),
    path('<int:produto_id>/delete', views.delete_produto, name="delete_produto" ),
    path('create-categoria', views.create_categoria, name='create_categoria')
]
