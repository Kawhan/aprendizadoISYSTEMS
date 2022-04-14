// Write a function that takes a number (a) as argument
// Split a into its individual digits and return them in an array
// Tipp: you might want to change the type of the number for the splitting
function myFunction(a) {
    return a
        .toString()
        .split("")
        .map((n) => {
            return Number(n);
        });
}

console.log(myFunction(10));
console.log(myFunction(931));
console.log(myFunction(193278));

// ------------------------------

function myFunction2(a) {
    const string = a + "";
    const strings = string.split("");
    return strings.map((digit) => Number(digit));
}

console.log(myFunction2(10));
console.log(myFunction2(931));
console.log(myFunction2(193278));
