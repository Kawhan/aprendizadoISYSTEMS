package main

import (
	"net/http"
	"text/template"
)

type Produto struct {
	Nome       string
	Descricao  string
	Preco      float64
	Quantidade int
}

var temp = template.Must(template.ParseGlob("templates/*.html"))

func main() {
	http.HandleFunc("/", index)

	http.ListenAndServe(":8000", nil)
}

func index(w http.ResponseWriter, r *http.Request) {
	produtos := []Produto{
		{
			Nome:       "Camiseta",
			Descricao:  "Azul bem bonita",
			Preco:      39,
			Quantidade: 5,
		},
		{
			"Tenis",
			"Confortavel",
			89,
			3,
		},
		{
			"Fone",
			"Muito bom",
			59,
			2,
		},
		{
			"Produto Novo",
			"Muito legal",
			1.99,
			1,
		},
	}

	temp.ExecuteTemplate(w, "index", produtos)
}
