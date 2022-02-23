let x = "";
console.log(x);
x = "oi";

// Declaração de função

                     //String --> parametro
function imprimeTexto (nome) {
    console.log(nome);
}
            // argumentos
imprimeTexto("Kawhan");
imprimeTexto("Kassio");

function somaNumeros () {
    const resultado = 2+2;
    return resultado; // retorno da função, pode só retornar algo sem ser uma variável
}

console.log(somaNumeros());
imprimeTexto(somaNumeros());