package main

import (
	"fmt"

	c "myProject/src/mylib"
)

func main() {
	contaDoKawhan := c.ContaCorrente{
		Titular: "Kawhan",
		Saldo:   300.00,
	}

	contaDoKawhan2 := c.ContaCorrente{
		Titular: "Kawhan2",
		Saldo:   400.00,
	}

	status := contaDoKawhan.Transferir(-600, &contaDoKawhan2)

	fmt.Println(status)
	fmt.Println(contaDoKawhan)
	fmt.Println(contaDoKawhan2)
}
