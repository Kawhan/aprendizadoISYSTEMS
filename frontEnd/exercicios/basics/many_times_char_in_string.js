// Write a function that takes two strings (a and b) as arguments
// Return the number of times a occurs in b
function myFunction(a, b) {
    let num = 0;
    let i = 0;
    while (i < b.length) {
        if (b[i] === a) num++;
        i++;
    }
    return num;
}

console.log(
    myFunction("m", "how many times does the character occur in this sentence?")
);

// ---------------------------------------------
function myFunction2(a, b) {
    return b.split(a).length - 1;
}

console.log(
    myFunction2(
        "m",
        "how many times does the character occur in this sentence?"
    )
);
