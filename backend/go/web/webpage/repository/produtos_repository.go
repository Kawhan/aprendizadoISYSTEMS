package repository

import (
	"database/sql"
	m "test/models"
)

type ProdutosRepository struct {
	TableName string
	Client    *sql.DB
}

func (repo *ProdutosRepository) BuscaProdutos() []m.Produto {
	// Executando uma query no banco de dados
	slcProducts, err := repo.Client.Query("select * from " + repo.TableName + " order by id asc")
	if err != nil {
		panic(err.Error())
	}

	p := m.Produto{}
	produtos := []m.Produto{}

	// Lendo cada produto
	for slcProducts.Next() {
		var id, quantidade int
		var nome, descricao string
		var preco float64

		err = slcProducts.Scan(&id, &nome, &descricao, &preco, &quantidade)
		if err != nil {
			panic(err.Error())
		}

		p.Id = id
		p.Nome = nome
		p.Descricao = descricao
		p.Preco = preco
		p.Quantidade = quantidade
		produtos = append(produtos, p)
	}

	return produtos
}

func (repo *ProdutosRepository) Insert(nome string, descricao string, preco_covertido float64, quantidadeConvertida int) {
	insert, err := repo.Client.Prepare("Insert into produtos(nome, descricao, preco, quantidade) VALUES($1, $2, $3, $4)")

	if err != nil {
		panic(err.Error())
	}

	insert.Exec(nome, descricao, preco_covertido, quantidadeConvertida)
}

func (repo *ProdutosRepository) Delete(id string) {
	delete, err := repo.Client.Prepare("delete from produtos where id=$1")

	if err != nil {
		panic(err.Error())
	}

	delete.Exec(id)
}

func (repo *ProdutosRepository) Edit(id string) m.Produto {
	produtoBancoDados, err := repo.Client.Query("select * from produtos where id=$1", id)
	if err != nil {
		panic(err.Error())
	}

	produtoParaAtualizar := m.Produto{}

	for produtoBancoDados.Next() {
		var id, quantidade int
		var nome, descricao string
		var preco float64

		err = produtoBancoDados.Scan(&id, &nome, &descricao, &preco, &quantidade)
		if err != nil {
			panic(err.Error())
		}

		produtoParaAtualizar.Id = id
		produtoParaAtualizar.Nome = nome
		produtoParaAtualizar.Descricao = descricao
		produtoParaAtualizar.Preco = preco
		produtoParaAtualizar.Quantidade = quantidade
	}

	return produtoParaAtualizar
}

func (repo *ProdutosRepository) AtualizaProduto(id int, nome string, descricao string, preco_covertido float64, quantidadeConvertida int) {
	atualizaProduto, err := repo.Client.Prepare("update produtos set nome=$1, descricao=$2, preco=$3, quantidade=$4 where id=$5")

	if err != nil {
		panic(err.Error())
	}

	atualizaProduto.Exec(nome, descricao, preco_covertido, quantidadeConvertida, id)
}
