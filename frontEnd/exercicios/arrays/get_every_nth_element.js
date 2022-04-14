// Write a function that takes an array (a) and a value (n) as arguments
// Save every nth element in a new array
// Return the new array
function myFunction(a, n) {
    let new_array = [];

    for (let i = n - 1; i < a.length; i += n) {
        new_array.push(a[i]);
    }
    return new_array;
}

console.log(myFunction([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3));
console.log(myFunction([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5));
console.log(myFunction([7, 2, 1, 6, 3, 4, 5, 8, 9, 10], 2));

// ============================================================
function myFunction2(a, n) {
    let rest = [...a];
    let result = [];
    for (let i = 0; i < a.length; i++) {
        if (rest.length < n) break;
        result.push(rest[n - 1]);
        rest = rest.slice(n);
    }
    return result;
}

console.log(myFunction2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3));
console.log(myFunction2([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5));
console.log(myFunction2([7, 2, 1, 6, 3, 4, 5, 8, 9, 10], 2));
