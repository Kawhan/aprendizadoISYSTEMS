const nomes = ['Ana', 'Marcos', 'Maria', 'Mauro'];
const notas = [7, 4, 5, 8, 7.5];

const nomes_2 = ['Ana', 'Marcos', 'Maria', 'Mauro'];
const altura = [1.60, 1.80, 1.62, 1.93, 1.70];

// Filter retorna para gente uma lista, e vem de filtrar resultados
// Precisa de uma função ou seja é um callback
// Para filtrar precisamos passar outra informação nesse caso foi nosso indice que pelo array notas vai selecionar as notas que são consideradas baixas para aprovação
// Ele funciona com base no true ou no false
const reprovados = nomes.filter( (aluno,indice) => 
    notas[indice] < 5
)

const baixos = nomes_2.filter( (nome,indice) => 
    altura[indice] < 1.70
)

console.log(`reprovados: ${reprovados}`)
console.log(`Abaixo da altura normal: ${baixos}`)