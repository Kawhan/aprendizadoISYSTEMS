package main

import (
	"fmt"
	"time"
)

/*
dia (com zero)	02
dia (sem o zero)	2
dia da semana (inteiro)	Monday
dia da semana abreviado	Mon
mês com número (com zero)	01
mês com número (sem zero)	1
mês (nome inteiro)	January
mês (nome abreviado)	Jan
ano (inteiro)	2006
ano (abreviado)	06
hora (com zero)	03
hora (sem zero)	3
hora (formato 24 horas)	15
minutos (com zero)	04
minutos (sem zero)	4
segundos (com zero)	05
segundos (sem zero)	5


*/

func main() {
	data := time.Now()
	fmt.Println(data.Format(("02/Jan/2006 15:04:05 ")))
}
