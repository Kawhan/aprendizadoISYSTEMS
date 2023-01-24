package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	imprimeCabecalho()

	iniciaBiblioteca()
}

func imprimeCabecalho() {
	nomeBiblioca := "DCX"

	fmt.Println("Seja bem vindo a biblioteca", nomeBiblioca)

}

func imprimeMenu() {
	fmt.Println("Escolha uma das opcoes:")
	fmt.Println("1- Listar todos os livros da biblioteca:")
	fmt.Println("2- Cadastrar livros da biblioteca:")
	fmt.Println("3- Retirar Livro:")
	fmt.Println("4- Sair do programa:")
}

func iniciaBiblioteca() {
	for {
		fmt.Println()
		imprimeMenu()

		opcao := leOpcaoUsuario()

		switch opcao {
		case 1:
			fmt.Println("Lendo os livros da biblioteca")
			listaLivros()
		case 2:
			fmt.Println("Digite o livro que deseja adicionar")
			escreveLivro()
		case 3:
			fmt.Println("Digite a linha que deseja remover")
		case 4:
			fmt.Println("Saindo do programa")
			os.Exit(0)
		}
	}
}

func leOpcaoUsuario() int {
	var opcao int

	fmt.Scan(&opcao)

	fmt.Println("\nSua opcao foi:", opcao)
	return opcao
}

func listaLivros() {
	fmt.Println("Listando Livros: ")

	livros := leListaLivros()

	for i, livro := range livros {
		fmt.Println("Livro de indice:", i, "é:", livro)
	}
}

func leListaLivros() []string {
	arquivo, err := os.Open("books.txt")
	var livros []string

	if err != nil {
		fmt.Println("Ocorreu um erro:", err)
	}

	leitor := bufio.NewReader(arquivo)

	for {
		linha, err := leitor.ReadString('\n')
		linha = strings.TrimSpace(linha)

		livros = append(livros, linha)

		if err == io.EOF {
			break
		}

	}

	arquivo.Close()

	return livros
}

func escreveLivro() {
	livro := lerLivrosUsuario()

	arquivo, err := os.OpenFile("books.txt", os.O_RDWR|os.O_APPEND, 0666)

	if err != nil {
		fmt.Println("Ocorreu um erro", err)
	}

	arquivo.WriteString("\n" + livro)
	arquivo.Close()
}

func lerLivrosUsuario() string {
	var livro string

	fmt.Scan(&livro)

	fmt.Println("O livro que você digitou foi: ", livro)

	return livro
}
