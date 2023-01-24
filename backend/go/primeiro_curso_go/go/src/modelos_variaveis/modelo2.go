package main

import (
	"fmt"
)

func main() {
	var (
		idade  int
		altura float32
		nome   string
	)

	idade = 15
	altura = 1.78
	nome = "Guilherme"

	fmt.Println(nome, idade, altura)
}
