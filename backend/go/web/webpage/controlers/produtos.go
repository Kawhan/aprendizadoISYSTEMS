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
	produtos := s.ProductRepository.BuscaProdutos()
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

func (s *Database) Delete(w http.ResponseWriter, r *http.Request) {
	idDoProduto := r.URL.Query().Get("id")
	s.ProductRepository.Delete(idDoProduto)
	http.Redirect(w, r, "/", 301)
}

func (s *Database) Edit(w http.ResponseWriter, r *http.Request) {
	idDoProduto := r.URL.Query().Get("id")
	produto := s.ProductRepository.Edit(idDoProduto)
	temp.ExecuteTemplate(w, "Edit", produto)
}

func (s *Database) Update(w http.ResponseWriter, r *http.Request) {
	if r.Method == "POST" {
		id := r.FormValue("id")
		nome := r.FormValue("nome")
		descricao := r.FormValue("descricao")
		preco := r.FormValue("preco")
		quantidade := r.FormValue("quantidade")

		idConvertido, err := strconv.Atoi(id)

		if err != nil {
			log.Println("Erro na conversão do id para int: ", err)
		}

		precoCovertido, err := strconv.ParseFloat(preco, 64)

		if err != nil {
			log.Println("Error na conversão do preço: ", err)
		}

		quantidadeConvertida, err := strconv.Atoi(quantidade)

		if err != nil {
			log.Println("Error na conversão da quantidade: ", err)
		}

		s.ProductRepository.AtualizaProduto(idConvertido, nome, descricao, precoCovertido, quantidadeConvertida)

	}

	http.Redirect(w, r, "/", 301)
}
