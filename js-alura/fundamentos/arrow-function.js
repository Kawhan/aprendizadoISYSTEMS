function apresentacao(nome) {
    return `meu nome é ${nome}`;
}

console.log(apresentacao('kawhan'));


// Arrow function
// Ela não pode ser nomeada e sempre é antecedida de uma const
// Ela tem o uso em alguns casos especiais
// Se a função tiver somente uma linha de código e não tiver return não precisamos das chaves
// Se a função tiver 1 parametro não precisamos colocar entre ()

                     // parametro
const apresentarArrow = nome => `meu nome é ${nome}`;
const soma = (num1, num2) => num1 + num2;

// Arrow function com mais de uma linha de instrução

const somaNumerosPequenos = (num1, num2) => {
    if (num1 || num2 > 10) {
        return "somente números de 1 a 9"
    }
    else {
        return num1 + num2;
    }
};

// Hoisting: arrow funcitoon se comporta como expressão

console.log(somaNumerosPequenos(1, 9));
console.log(somaNumerosPequenos(11, 9));
console.log(somaNumerosPequenos(1, 11));