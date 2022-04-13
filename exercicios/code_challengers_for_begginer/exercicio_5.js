// Create a function that reverses an array

function reveseArray(arr) {
    let valor = arr;
    let valor2 = [];

    for (let j = valor.length - 1; j >= 0; j--) {
        valor2.push(valor[j]);
    }

    return valor2;
}

console.log(reveseArray([1, 3, 2, 4, 5, 6]));
