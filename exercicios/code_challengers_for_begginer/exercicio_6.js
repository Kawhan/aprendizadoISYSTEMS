// Sort an array from lowest to highes
function sortValues(arr) {
    let valor = arr;
    let temp;

    for (let i = 0; i < valor.length; i++) {
        for (let j = 0; j < valor.length; j++) {
            if (valor[i] <= valor[j]) {
                temp = valor[i];
                valor[i] = valor[j];
                valor[j] = temp;
            }
        }
    }

    return valor;
}

console.log(sortValues([-11, 5, 4, 3, 2]));
