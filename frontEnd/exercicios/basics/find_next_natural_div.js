// Write a function that takes two numbers, say x and y, as arguments
// Check if x is divisible by y
// If yes, return x
// If not, return the next higher natural number that is divisible by y
function myFunction(x, y) {
    if (x % y === 0) {
        return x;
    } else {
        while (!(x % y === 0)) {
            x++;
        }
        return x;
    }
}

console.log(myFunction(1, 23));
console.log(myFunction(23, 23));
console.log(myFunction(7, 3));
console.log(myFunction(-5, 7));

// ====================================

function myFunction2(x, y) {
    while (x % y !== 0) x++;
    return x;
}

console.log(myFunction2(1, 23));
console.log(myFunction2(23, 23));
console.log(myFunction2(7, 3));
console.log(myFunction2(-5, 7));
