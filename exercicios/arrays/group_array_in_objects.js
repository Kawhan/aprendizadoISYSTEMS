// Write a function that takes an array of strings as argument
// Group those strings by their first letter
// Return an object that contains properties with keys representing first letters
// The values should be arrays of strings containing only the corresponding strings
// For example, the array ['Alf', 'Alice', 'Ben'] should be transformed to
// { a: ['Alf', 'Alice'], b: ['Ben']}
function myFunction(arr) {
    let array = [];
    let letter;
    let cont = 0;
    letter = new Object();

    let valor = arr.forEach((element) => {
        for (let i = 0; i < arr.length; i++) {
            arr[i][i] === 
        }
        
        letter[element[0].toLowerCase()] = element;

        array.push(letter);

        cont++;
    });

    return array;
}

console.log(myFunction(["Alf", "Alice", "Ben"]));
