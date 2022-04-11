// Write a function that takes a string as argument
// As it is, the string has no meaning
// Increment each letter to the next letter in the alphabet
// Return the correct word
function myFunction(str) {
    let aux;
    let String_2 = "";

    for (let i = 0; i < str.length; i++) {
        aux = str.charCodeAt(i) + 1;
        String_2 += String.fromCharCode(aux);
    }
    return String_2;
}

console.log(myFunction("bnchmf"));
console.log(myFunction("bgddrd"));
console.log(myFunction("sdrshmf"));

// ---------------------------------------------

function myFunction2(str) {
    const arr = [...str];
    const correctedArray = arr.map((e) =>
        String.fromCharCode(e.charCodeAt() + 1)
    );
    return correctedArray.join("");
}

console.log(myFunction2("bnchmf"));
console.log(myFunction2("bgddrd"));
console.log(myFunction2("sdrshmf"));
