// Write a function that takes an array (a) and a number (b) as arguments
// Sum up all array elements with a value greater than b
// Return the sum
function myFunction(a, b) {
    let sum = 0;
    a.forEach((element) => {
        if (element > b) {
            sum += element;
        }
    });
    return sum;
}

console.log(myFunction([1, 2, 3, 4, 5, 6, 7], 2));
console.log(myFunction([-10, -11, -3, 1, -4], -3));
console.log(myFunction([78, 99, 100, 101, 401], 99));

// =========================================================
function myFunction2(a, b) {
    return a.reduce((sum, cur) => {
        if (cur > b) return sum + cur;
        return sum;
    }, 0);
}

console.log(myFunction2([1, 2, 3, 4, 5, 6, 7], 2));
console.log(myFunction2([-10, -11, -3, 1, -4], -3));
console.log(myFunction2([78, 99, 100, 101, 401], 99));
