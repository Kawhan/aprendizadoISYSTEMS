// Conversão em promessa

// Se o valor não for um Promise, ele converterá o valor em um resolvido Promisee aguardará por ele.]

async function f3() {
    var y = await 20;
    console.log(y); // 20
}

f3();
