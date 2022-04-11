// Write a function that takes two numbers (min and max) as arguments
// Return an array of numbers in the range min to max
function myFunction(min, max) {
    let array = [];

    for (let i = min; i <= max; i++) {
        array.push(i);
    }
    return array;
}

console.log(myFunction(2, 10));
console.log(myFunction(1, 3));
console.log(myFunction(-5, 5));
console.log(myFunction(2, 7));

// =========================================
function myFunction2(min, max) {
    let arr = [];
    for (let i = min; i <= max; i++) {
        arr.push(i);
    }
    return arr;
}

console.log(myFunction2(2, 10));
console.log(myFunction2(1, 3));
console.log(myFunction2(-5, 5));
console.log(myFunction2(2, 7));
