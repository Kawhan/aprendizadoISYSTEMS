// Write a function that takes a string (a) as argument
// Get the first 3 characters of a
// Return the result
function myFunction(a) {
    return a[0] + a[1] + a[2];
}

console.log(myFunction("abcdefg"));

// --------------------------------------

function myFunction2(a) {
    return a.slice(0, 3);
}

console.log(myFunction2("abcdefg"));
