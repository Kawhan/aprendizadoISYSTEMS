from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.listarProdutos, name='produtos'),
    path('categoria', views.listarCategoria, name='categoria'),
    path('<int:produto_id>/view-produto', views.informacao, name='informacao'),
    path('create-produto', views.create_produto, name='create_produto'),
    path('<int:produto_id>/change-produto', views.change_produto, name='change_produto'),
    path('<int:produto_id>/delete-produto', views.delete_produto, name="delete_produto" ),
    path('<int:categoria_id>/change-categoria', views.change_categoria, name='change_categoria'),
    path('create-categoria', views.create_categoria, name='create_categoria'),
    path('<int:categoria_id>/delete-categoria', views.delete_categoria, name="delete_categoria" ),
    path('<int:categoria_id>/view-categoria', views.view_categoria, name="view_categoria"),
    path('search', views.search, name="search"),
]
