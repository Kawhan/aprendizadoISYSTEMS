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
	slcProducts, err := repo.Client.Query("select * from " + repo.TableName)
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
