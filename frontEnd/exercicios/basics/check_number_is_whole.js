// Write a function that takes a number (a) as argument
// If a is a whole number (has no decimal place), return true
// Otherwise, return false
function myFunction(a) {
    return a.toString().split(".").length - 1 === 0;
}

console.log(myFunction(1.123));
console.log(myFunction(5));

// --------------------------------------

function myFunction2(a) {
    return a - Math.floor(a) === 0;
}

console.log(myFunction2(1.123));
console.log(myFunction2(5));
