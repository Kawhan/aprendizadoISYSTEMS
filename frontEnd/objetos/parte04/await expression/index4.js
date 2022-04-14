// Rejeição da promessa

// Se Promisefor rejeitado, o valor rejeitado será lançado.

async function f4() {
    try {
        var z = await Promise.reject(30);
    } catch (e) {
        console.error(e); // 30
    }
}

f4();
