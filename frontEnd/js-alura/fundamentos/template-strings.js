// template é uma string modelo

const nome = "Kawhan";
const idade = 2022 - 1999;
const cidadeDeNascimento = "Itaporanga";

const apresentacao = "meu nome é " + nome + ", minha idade é " + idade + " anos e nasci na cidade de " + cidadeDeNascimento;

console.log(apresentacao);

console.log(`Meu nome é ${nome}, minha idade é ${idade} anos e nasci na cidade de ${cidadeDeNascimento}`);

const apresentacaoTemplate = `Meu nome é ${nome}, minha idade é ${idade} anos e nasci na cidade de ${cidadeDeNascimento}`;

console.log(apresentacaoTemplate);