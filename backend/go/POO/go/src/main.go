package main

import (
	"fmt"

	t "myProject/src/cliente"
	c "myProject/src/contas"
)

func main() {
	clienteBruno := t.Titular{
		Nome:      "Bruno",
		CPF:       "123456",
		Profissao: "Desenvolvedor",
	}

	contaDoBruno := c.ContaCorrente{
		Titular:       clienteBruno,
		NumeroAgencia: 1234,
		NumeroConta:   3,
		Saldo:         200.00,
	}

	// contaDoBruno := c.ContaCorrente{
	// 	Titular: t.Titular{
	// 		Nome:      "Kawhan",
	// 		CPF:       "1234567",
	// 		Profissao: "Bancario",
	// 	},
	// 	NumeroAgencia: 1234,
	// 	NumeroConta:   3,
	// 	Saldo:         200.00,
	// }

	fmt.Println(contaDoBruno)
}
