// Conversão de tipos

// conversão implicita
// Permite que a gente converta um tipo de dado em outro
// == só compara o valor, ou seja o que esta dentro
// === compara tipo e valor

const numero = 456;
const numeroString = Number("456");

console.log(numero == numeroString);
console.log(numero === numeroString);

console.log(numero + numeroString);

// Number()
console.log(numero + Number(numeroString));

// String()