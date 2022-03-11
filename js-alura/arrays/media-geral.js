const salaJS = [7,8,8,7,10,6.5, 4, 10, 7];
const salaJava = [6,5,8,9,5,6];
const salaPython = [7, 3.5, 8, 9.5];

function mediaSala (notasDaSala) {
    // Metodo reduce vai reduzir todos os valores do nosso array para um único valor númerico
    // Reduce sempre vai ter de ter 2 valores o primeiro é o acumulador e o segundo é atual
    // Reduce itera faz um loop no nosso array
    // o 0 representa um valor neutro que vai ser acumulado
    const somaDasNotas = notasDaSala.reduce((acumulador, atual) => 
    atual + acumulador,0)
    return somaDasNotas/notasDaSala.length
    
}

//O método reduce() está trabalhando com dois parâmetros. O primeiro é a função callback obrigatória para retornar o cálculo e o segundo parâmetro é um número que representa o valor inicial - no caso, 0.

//A função callback foi escrita diretamente dentro do reduce(), e esta função também está recebendo dois parâmetros, ambos obrigatórios: O valor acumulado e o valor atual.

//A função callback foi escrita na forma de arrow function; nesse caso, quando só temos uma linha de instrução dentro da função (atual + acum) não precisamos usar chaves e nem da palavra-chave return.

//Caso você tenha mais de uma linha de instrução dentro de uma arrow function, as chaves {} e a palavra-chave return voltam a ser necessários.

console.log(`Média da sala de Javascript ${mediaSala(salaJS)}`);
console.log(`Média da sala de Java ${mediaSala(salaJava)}`);
console.log(`Média da sala de Python ${mediaSala(salaPython)}`);

const notas = [10, 6.5, 8 ,7];

const media = notas.reduce((acum, atual) => atual + acum, 0) / notas.length;

console.log(media);


const numeros = [10, 6.5, 8 ,7];

function operacaoNumerica(acum, atual) {
    return atual + acum
}
   
const soma = numeros.reduce(operacaoNumerica, 0)
console.log(soma);