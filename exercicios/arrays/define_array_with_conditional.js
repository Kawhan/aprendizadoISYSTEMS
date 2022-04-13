// Write a function that takes an array with arbitrary elements and a number as arguments
// Return a new array, the first element should be either the given number itself
// or zero if the number is smaller than 6
// The other elements should be the elements of the original array
// Try not to mutate the original array
function myFunction(arr, num) {
    let new_array = arr;

    if (num < 6) {
        new_array.unshift(0);
    } else {
        new_array.unshift(num);
    }
    return new_array;
}

console.log(myFunction([1, 2, 3], 6));
console.log(myFunction(["a", "b"], 2));
console.log(myFunction([null, false], 11));

// ===============================================
function myFunction2(arr, num) {
    return [...(num > 5 ? [num] : [0]), ...arr];
}

console.log(myFunction2([1, 2, 3], 6));
console.log(myFunction2(["a", "b"], 2));
console.log(myFunction2([null, false], 11));
