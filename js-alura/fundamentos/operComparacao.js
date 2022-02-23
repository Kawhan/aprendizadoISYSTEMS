// Os 2 iguais (==) faz a comparação e faz aquela conversão implicita (comparação implicita)

const numero = 5;
const textoNumero = '5';

console.log(numero == textoNumero);

// Os 3 iguais (===) faz a comparação mais real e literal, dando diferente caso o type das comparações sejam diferentes (comparação explicita)

console.log(numero === textoNumero);

//typeof para ver o tipo de dado de nossa váriavel
console.log(typeof numero);
console.log(typeof textoNumero);

// == compara somente o valor
// === compara o valor e o tipo de dado