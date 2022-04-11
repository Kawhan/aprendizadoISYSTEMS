// Write a function that takes an array (a) and a value (b) as argument
// The function should clean a from all occurrences of b
// Return the filtered array
function myFunction(a, b) {
    for (let i = 0; i < a.length; i++) {
        if (a[i] === b) {
            a.splice(i, 1);
        }
    }
    return a;
}

console.log(myFunction([1, 2, 3], 2));
console.log(myFunction([1, 2, "2"], "2"));
console.log(myFunction([false, "2", 1], false));
console.log(myFunction([1, 2, "2", 1], 1));

// =================================================
function myFunction2(a, b) {
    return a.filter((cur) => cur !== b);
}

console.log(myFunction2([1, 2, 3], 2));
console.log(myFunction2([1, 2, "2"], "2"));
console.log(myFunction2([false, "2", 1], false));
console.log(myFunction2([1, 2, "2", 1], 1));
