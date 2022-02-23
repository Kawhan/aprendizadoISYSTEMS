
            // argumentos
function soma (num1, num2) {
    return num1 + num2;
}
            //   parametros
console.log(soma (2, 2));
console.log(soma (4, 8));
console.log(soma (10, 12));

// parâmetros x argumentos

// Ordem dos parâmetros

function nomeIdade (nome, idade) {
    return `meu nome é ${nome} e minha idade é ${idade}`;
}

console.log(nomeIdade('Kawhan', 22));

function multiplica(num1 = 1, num2 = 1) {
    return num1 * num2;
}

console.log(multiplica(soma (4, 5), soma (3, 3)));