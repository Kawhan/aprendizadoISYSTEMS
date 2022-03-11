const notas = [10, 9, 8, 7, 6];

// Ela é uma função call back ou seja chama uma função
// For each  é um metodo que não retorna nada por sí,  ele simplesmente execulta o que esta dentro do bloco
// Tudo que o método map faz é retornado como uma nova array
const notasAtualizadas = notas.map(nota => {
    nota == 10 ? nota : ++nota;
    return nota;
});

const multiplicaNotas = notas.map(nota => nota * 10);

const multiplicaNotas_2 = notas.map(function (nota) {
    nota = nota*10;
    return nota;
});

console.log(notasAtualizadas);
console.log(multiplicaNotas);
console.log(multiplicaNotas_2);