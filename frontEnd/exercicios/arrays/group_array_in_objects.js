// Write a function that takes an array of strings as argument
// Group those strings by their first letter
// Return an object that contains properties with keys representing first letters
// The values should be arrays of strings containing only the corresponding strings
// For example, the array ['Alf', 'Alice', 'Ben'] should be transformed to
// { a: ['Alf', 'Alice'], b: ['Ben']}
function myFunction(arr) {
    let letter;
    let cont = 0;
    letter = new Object();

    let valor = arr.forEach((element) => {
        if (letter[element[0].toLowerCase()]) {
        } else {
            letter[element[0].toLowerCase()] = [];
        }

        for (const property in letter) {
            if (property === element[0].toLowerCase()) {
                letter[property].push(element);
            }
        }

        cont++;
    });

    return letter;
}

console.log(myFunction(["Alf", "Alice", "Ben"]));
console.log(myFunction(["Ant", "Bear", "Bird"]));
console.log(myFunction(["Berlin", "Paris", "Prague"]));

// ====================================================
function myFunction2(arr) {
    return arr.reduce((acc, cur) => {
        const firstLetter = cur.toLowerCase().charAt(0);
        return { ...acc, [firstLetter]: [...(acc[firstLetter] || []), cur] };
    }, {});
}

console.log(myFunction2(["Alf", "Alice", "Ben"]));
console.log(myFunction2(["Ant", "Bear", "Bird"]));
console.log(myFunction2(["Berlin", "Paris", "Prague"]));
