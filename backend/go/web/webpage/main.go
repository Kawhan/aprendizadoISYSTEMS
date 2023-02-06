package main

import (
	"net/http"
	c "test/controlers"
	db "test/db"
	"test/repository"
	r "test/routes"
)

func main() {
	db := db.ConectaComBancoDeDados()

	server := c.Database{
		ProductRepository: repository.ProdutosRepository{
			TableName: "produtos",
			Client:    db,
		},
	}
	r.CarregaRotas(&server)
	http.ListenAndServe(":8000", nil)

	db.Close()
}
