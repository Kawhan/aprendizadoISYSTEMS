from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('produtos', listarProdutos, name='produtos'),
    path('categoria', listarCategoria, name='categoria'),
    path('<int:produto_id>/view-produto', informacao, name='informacao'),
    path('create-produto', create_produto, name='create_produto'),
    path('<int:produto_id>/change-produto', change_produto, name='change_produto'),
    path('<int:produto_id>/delete-produto', delete_produto, name="delete_produto" ),
    path('<int:categoria_id>/change-categoria', change_categoria, name='change_categoria'),
    path('create-categoria', create_categoria, name='create_categoria'),
    path('<int:categoria_id>/delete-categoria', delete_categoria, name="delete_categoria" ),
    path('<int:categoria_id>/view-categoria', view_categoria, name="view_categoria"),
    path('search', search, name="search"),
    path('create-produto-api/', create_produtos_api, name="create_produtos_api"),
    path('view-produto-api/', produtos_view_api, name="view_produtos_api"),
    path('view-categoria-api/', categoria_view_api, name="view_categoria_api"),
]
