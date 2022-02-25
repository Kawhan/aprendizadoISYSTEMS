const alunos = ['João', 'Juliana', 'Caio', 'Ana'];

const mediasDosAlunos = [10, 7, 9 ,6];

                    // 0[alunos]   1[mediasDosAlunos]
let listaDeNotasEAlunos = [alunos, mediasDosAlunos];

// includes -> retorna um booleano
// indexOf -> retorna o indice do elemento


const exibeNomeNotas = (nomeDoAluno) => {
    if (listaDeNotasEAlunos[0].includes(nomeDoAluno)) {
        let indice = listaDeNotasEAlunos[0].indexOf(nomeDoAluno)
        return listaDeNotasEAlunos[0][indice] + ', sua média é ' + listaDeNotasEAlunos[1][indice];
    }
    else {
        return "Aluno não esta cadastrado";
    }
};

console.log(exibeNomeNotas("Ana"));
console.log(exibeNomeNotas("Nemo"));