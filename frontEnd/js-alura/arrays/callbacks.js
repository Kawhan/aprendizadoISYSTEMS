const nomes = ["Ana", "Ju", "Leo", "Paula"];

nomes.forEach(imprimeNomes)

function imprimeNomes (nome) {
    console.log(nome);
}

const notas = [10, 9, 8 ,7 ,6];

const notasAtualizadas = notas.map( nota => nota + 1)

console.log(notasAtualizadas)