package controlers

import (
	"log"
	"net/http"
	"strconv"
	r "test/repository"
	"text/template"
)

type Database struct {
	ProductRepository r.ProdutosRepository
}

var temp = template.Must(template.ParseGlob("templates/*.html"))

func (s *Database) Index(w http.ResponseWriter, r *http.Request) {
	// produtos := models.BuscaProdutos()
	produtos := s.ProductRepository.BuscaProdutos()

	// fmt.Println(produtos)
	temp.ExecuteTemplate(w, "index", produtos)
}

func (s *Database) New(w http.ResponseWriter, r *http.Request) {
	temp.ExecuteTemplate(w, "New", nil)
}

func (s *Database) Insert(w http.ResponseWriter, r *http.Request) {
	if r.Method == "POST" {
		nome := r.FormValue("nome")
		descricao := r.FormValue("descricao")
		preco := r.FormValue("preco")
		quantidade := r.FormValue("quantidade")

		precoCovertido, err := strconv.ParseFloat(preco, 64)

		if err != nil {
			log.Println("Error na conversão do preço: ", err)
		}

		quantidadeConvertida, err := strconv.Atoi(quantidade)

		if err != nil {
			log.Println("Error na conversão da quantidade: ", err)
		}

		s.ProductRepository.Insert(nome, descricao, precoCovertido, quantidadeConvertida)
	}
	http.Redirect(w, r, "/", 301)
}
