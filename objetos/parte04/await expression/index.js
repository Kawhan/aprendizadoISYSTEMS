// Aguardando uma promessa a ser cumprida
// Se a Promisefor passado para uma awaitexpressão, ele aguardará o Promisepreenchimento e retornará o valor preenchido

function resolveAfter2Seconds(x) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(x);
        }, 2000);
    });
}

async function f1() {
    var x = await resolveAfter2Seconds(10);
    console.log(x); // 10
}

f1();
