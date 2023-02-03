package main

import (
	"fmt"
	"strconv"
)

/*
 salarioConvertido, err := strconv.ParseFloat(salario, 64)
    if err != nil {
        fmt.Println(err)
    }
    aumentoConvertido, err := strconv.ParseFloat(aumento, 64)
    if err != nil {
        fmt.Println(err)
    }


*/

func main() {
	salario := "1000"
	aumento := "20"

	salarioConvertido, err := strconv.Atoi(salario)
	if err != nil {
		fmt.Println(err)
	}
	aumentoConvertido, err := strconv.Atoi(aumento)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("O salário é", salario, "e o aumento de", aumento+"%")

	novoSalario := ((salarioConvertido * aumentoConvertido) / 100) + salarioConvertido
	fmt.Println("O novo salário é", novoSalario)
}
