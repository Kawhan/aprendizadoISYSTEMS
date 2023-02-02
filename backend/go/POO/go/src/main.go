package main

import (
	"fmt"

	"myProject/src/contas"
)

func PagarBoleto(conta verificarConta, valorDoBoleto float64) {
	conta.Sacar(valorDoBoleto)
}

type verificarConta interface {
	Sacar(valor float64) string
}

func main() {
	contaExemplo := contas.ContaCorrente{}
	contaExemplo2 := contas.ContaPoupanca{}
	contaExemplo.Depositar(100)
	contaExemplo2.Depositar(200)
	PagarBoleto(&contaExemplo, 30)

	fmt.Println(contaExemplo.ObterSaldo())
	fmt.Println(contaExemplo2.ObterSaldo())
}
