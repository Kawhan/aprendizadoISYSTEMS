package main

import (
	"fmt"
	"strconv"
)

func main() {
	salario := "1000"
	aumento := "20"

	salarioConvertido, _ := strconv.Atoi(salario)
	aumentoConvertido, _ := strconv.Atoi(aumento)

	fmt.Println("O salário é", salario, "e o aumento de", aumento+"%")

	novoSalario := ((salarioConvertido * aumentoConvertido) / 100) + salarioConvertido
	fmt.Println("O novo salário é", novoSalario)
}
