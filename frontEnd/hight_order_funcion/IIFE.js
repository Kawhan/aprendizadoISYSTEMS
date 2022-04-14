//função normal
function adicionarJunto() {
    var x = 20;
    var y = 20;
    var resposta = x + y;
    console.log(resposta);
}
adicionarJunto();

// Quando temos uma função que no fundo só queremos usar ela uma vez e que ninguém mais consiga utilizar ela fazemos uma IFFE
// Que basicamente é um conceito que gira em torno de colocar funções sempre tem esse objetivo

(function addTogether() {
    var x = 20;
    var y = 20;
    var resposta = x + y;
    console.log(resposta);
});

// De qualquer forma, porque estamos criando uma daquelas expressões de função que acabei de dizer umas dez vezes, na verdade não precisamos mais dar um nome à função, porque o plano é que, uma vez que tenhamos criado um IIFE , tenhamos nenhuma intenção de chamar a função novamente. Então vamos nos livrar do nome:

(function () {
    var x = 20;
    var y = 20;
    var resposta = x + y;
    console.log(resposta);
});

// Finalmente, precisamos de uma maneira de chamar essa função, mas como fazemos isso agora, já que não temos um nome para referenciar? Bem, nós simplesmente adicionamos um par de colchetes no final da função (mas logo antes do ponto e vírgula), assim:

(function () {
    var x = 20;
    var y = 20;
    var resposta = x + y;
    console.log(resposta);
})();
