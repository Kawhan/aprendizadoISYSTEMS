// Write a function that takes arguments an arbitrary number of arrays
// It should return an array containing the values of all arrays
function myFunction(...arrays) {
    let complet_array = arrays[0];
    let valor = arrays.forEach((elements) => {
        for (let i = 0; i < elements.length; i++) {
            if (elements !== complet_array) {
                complet_array.push(elements[i]);
            }
        }
    });
    return complet_array;
}

console.log(myFunction([1, 2, 3], [4, 5, 6]));
console.log(myFunction(["a", "b", "c"], [4, 5, 6]));
console.log(myFunction([true, true], [1, 2], ["a", "b"]));

// ==========================================================
function myFunction2(...arrays) {
    return arrays.flat();
}

console.log(myFunction2([1, 2, 3], [4, 5, 6]));
console.log(myFunction2(["a", "b", "c"], [4, 5, 6]));
console.log(myFunction2([true, true], [1, 2], ["a", "b"]));
