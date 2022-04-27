// Para tratar erros que podem aparecer no seu código podemos usar o bloco try and catch
// é importante que você saiba que não é interessante exibir para o nosso usuário final os erros internos dos programas
// Não exiba essa erro para o usuário final

// try {
//     console.log(naoExisto);
// } catch (err) {
//     console.log("variavel não existe!");
// }

function soma(x, y) {
    if (typeof x !== "number" || typeof y !== "number") {
        // throw "x e y precisam ser números";
        throw new Error("x e y precisam ser números"); // Criando um novo error
        // No console aparece "Error: ...", se quisessemos que aparecesse outra coisa seria mudar essa parte
    }
    return x + y;
}

try {
    console.log(soma(2, 2));
    console.log(soma("1", 2));
    console.log(soma(1, "2"));
    console.log(soma("1", "2"));
} catch (err) {
    // Não é interessante manda para o usuário, porém no back end pode ser que ajude
    // console.log(err);
    console.log("Alguma coisa mais amigável pro usuário!");
}
