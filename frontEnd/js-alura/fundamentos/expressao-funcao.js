// Declaração de função
// funções e var são "listadas" no topo do nosso código

function minhaFuncao (param) {
    // bloco de código
}

minhaFuncao();


// Expressão de função

const soma = function(num1, num2) {
    return num1 + num2;
};

console.log(soma(2, 2));

// Diferença principal Hoisting

console.log(apresentar());

function apresentar () {
    return "ola";
}


console.log(multiplica(2, 2));

const multiplica = function(num1, num2) {
    return num1 * num2;
};