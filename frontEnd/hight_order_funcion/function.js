// Funções
const lukeLogin = () => {
    let array = [];
    for (i = 0; i < 90000; i++) {
        array.push(i);
    }
    return "Luke logado com sucesso!";
};

const leiaLogin = () => {
    let array = [];
    for (i = 0; i < 90000; i++) {
        array.push(i);
    }
    return "Leia logada com sucesso!";
};

// console.log(lukeLogin());
// console.log(leiaLogin());

//DRY, don’t repeat yourself
const usuarioLogin = (pessoa) => {
    let array = [];
    for (i = 0; i < 90000; i++) {
        array.push(i);
    }
    return `${pessoa} logou com sucesso no sistema!`;
};

// console.log(usuarioLogin("Luke"));

// High order function é aquela que é uma função que recebe um ou dois argumentos e retorna uma função como resultado

const acesso = (nome) => {
    return `${nome} logou com sucesso no sistema!`;
};

const autentica = (cargo) => {
    let array = [];
    for (i = 0; i < cargo; i++) {
        array.push(i);
    }
    return true;
};

const login = (pessoa, autentica) => {
    if (pessoa.cargo === `funcionario`) {
        autentica(9);
    } else if (pessoa.cargo === `diretoria`) {
        autentica(9);
    }
    return acesso(pessoa.nome);
};

console.log(login({ cargo: `diretoria`, nome: `Leia` }, autentica));

// High order functions são funções que recebem uma função ou mais como argumento, retornando outra função;
// Isso permite a composição de funções, ou seja, ter funções pequenas que compõem outras funções maiores;
// funções que são chamadas dentro de outra são chamadas callback functions, pois são “called back” (“chamadas de volta” em uma tradução livre) dentro da função onde estão compostas.
