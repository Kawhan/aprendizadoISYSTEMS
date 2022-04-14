// Write a function that takes two arrays as arguments
// Merge both arrays and remove duplicate values
// Sort the merge result in ascending order
// Return the resulting array
function myFunction(a, b) {
    for (let i = 0; i < b.length; i++) {
        for (let j = 0; j < a.length; j++) {
            if (b[i] === a[j]) {
                a.splice(j, 1);
            }
        }
    }

    let listas = a.concat(b);
    listas.sort(function (a, b) {
        return a - b;
    });
    return listas;
}

console.log(myFunction([1, 2, 3], [3, 4, 5]));
console.log(myFunction([-10, 22, 333, 42], [-11, 5, 22, 41, 42]));

// ==================================================================
function myFunction2(a, b) {
    return [...new Set([...a, ...b])].sort((x, y) => x - y);
}

console.log(myFunction2([1, 2, 3], [3, 4, 5]));
console.log(myFunction2([-10, 22, 333, 42], [-11, 5, 22, 41, 42]));
