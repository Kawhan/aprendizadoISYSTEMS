// Write a function that takes two arrays as arguments
// Merge both arrays and remove duplicate values
// Sort the merge result in ascending order
// Return the resulting array
function myFunction(a, b) {
    let indice = 0;
    let isValid = true;

    let valor = a.forEach((element) => {
        valor2 = b.forEach((element2) => {
            if (element == element2 || isValid) {
                indice = a.indexOf(element);
                isValid = false;
            }
        });
    });

    a.splice(indice, 1);
    let listas = a.concat(b);
    return listas.sort();
}

console.log(myFunction([1, 2, 3], [3, 4, 5]));
console.log(myFunction([-10, 22, 333, 42], [-11, 5, 22, 41, 42]));
