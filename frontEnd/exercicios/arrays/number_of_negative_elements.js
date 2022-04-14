// Write a function that takes an array of numbers as argument
// Return the number of negative values in the array
function myFunction(a) {
    let cont = 0;
    let valor = a.forEach((element) => {
        if (element < 0) {
            cont++;
        }
    });
    return cont;
}

console.log(myFunction([1, -2, 2, -4]));
console.log(myFunction([0, 9, 1]));
console.log(myFunction([4, -3, 2, 1, 0]));

// =============================================
function myFunction2(a) {
    return a.filter((el) => el < 0).length;
}

console.log(myFunction2([1, -2, 2, -4]));
console.log(myFunction2([0, 9, 1]));
console.log(myFunction2([4, -3, 2, 1, 0]));
