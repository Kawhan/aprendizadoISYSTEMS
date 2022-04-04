// Write a function that takes two strings (a and b) as arguments
// If a contains b, append b to the beginning of a
// If not, append it to the end
// Return the concatenation
function myFunction(a, b) {
    return a.includes(b) ? b + a : a + b;
}

console.log(myFunction("cheese", "cake"));
console.log(myFunction("lips", "s"));
console.log(myFunction("Java", "script"));
console.log(myFunction(" think, therefore I am", "I"));

// ------------------------------------------------------
function myFunction2(a, b) {
    return a.indexOf(b) === -1 ? a + b : b + a;
}

console.log(myFunction2("cheese", "cake"));
console.log(myFunction2("lips", "s"));
console.log(myFunction2("Java", "script"));
console.log(myFunction2(" think, therefore I am", "I"));
