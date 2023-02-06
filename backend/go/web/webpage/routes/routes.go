package routes

import (
	"net/http"
	c "test/controlers"
)

func CarregaRotas(server *c.Database) {

	http.HandleFunc("/", server.Index)
	http.HandleFunc("/new", server.New)
	http.HandleFunc("/insert", server.Insert)
}
