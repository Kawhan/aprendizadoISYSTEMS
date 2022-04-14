// Write a function that takes an array of objects as argument
// Sort the array by property b in ascending order
// Return the sorted array
function myFunction(arr) {
    let armazenamento = arr[0];
    let mudancas;
    let array = [];
    let isValid = false;

    let valor = arr.forEach((element) => {
        if (element.b !== armazenamento.b) {
            if (element.b < armazenamento.b) {
                mudancas = armazenamento;
                armazenamento = element;
                element = mudancas;
                array.push(armazenamento);
                array.push(element);
                isValid = false;
            }
        } else {
            isValid = true;
        }
    });

    if (isValid) {
        return arr;
    }

    if (!isValid) {
        return array;
    }
}

console.log(
    myFunction([
        { a: 1, b: 2 },
        { a: 5, b: 4 },
    ])
);

console.log(
    myFunction([
        { a: 2, b: 10 },
        { a: 5, b: 4 },
    ])
);

console.log(
    myFunction([
        { a: 1, b: 7 },
        { a: 2, b: 1 },
    ])
);

// ===========================================

function myFunction2(arr) {
    const sort = (x, y) => x.b - y.b;
    return arr.sort(sort);
}

console.log(
    myFunction2([
        { a: 1, b: 2 },
        { a: 5, b: 4 },
    ])
);

console.log(
    myFunction2([
        { a: 2, b: 10 },
        { a: 5, b: 4 },
    ])
);

console.log(
    myFunction2([
        { a: 1, b: 7 },
        { a: 2, b: 1 },
    ])
);
