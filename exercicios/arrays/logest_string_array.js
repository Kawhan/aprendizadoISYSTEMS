// Write a function that takes an array of strings as argument
// Return the longest string
function myFunction(arr) {
    let correct_element = arr[0];
    valor = arr.forEach((element) => {
        if (element.length > correct_element.length) {
            correct_element = element;
        }

        return correct_element;
    });
    return correct_element;
}

console.log(myFunction(["help", "me"]));
console.log(myFunction(["I", "need", "candy"]));

// =========================================================
function myFunction2(arr) {
    return arr.reduce((a, b) => (a.length <= b.length ? b : a));
}

console.log(myFunction2(["help", "me"]));
console.log(myFunction2(["I", "need", "candy"]));
