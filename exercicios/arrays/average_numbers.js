// Write a function that takes an array of numbers as argument
// It should return the average of the numbers
function myFunction(arr) {
    let contagem = 0;
    let valor = arr.forEach((value) => {
        contagem += value;
    });

    return contagem / arr.length;
}

console.log(myFunction([10, 100, 40]));
console.log(myFunction([10, 100, 1000]));
console.log(myFunction([-50, 0, 50, 200]));

// ==================================================
function myFunction2(arr) {
    return arr.reduce((acc, cur) => acc + cur, 0) / arr.length;
}

console.log(myFunction2([10, 100, 40]));
console.log(myFunction2([10, 100, 1000]));
console.log(myFunction2([-50, 0, 50, 200]));
