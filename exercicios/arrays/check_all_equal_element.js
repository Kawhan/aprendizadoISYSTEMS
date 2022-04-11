// Write a function that takes an array as argument
// It should return true if all elements in the array are equal
// It should return false otherwise
function myFunction(arr) {
    let correct_element = arr[0];
    let isVerify = true;

    let valor = arr.forEach((element) => {
        if (element === correct_element) {
            correct_element = element;
        } else {
            isVerify = false;
        }
    });

    return isVerify;
}

console.log(myFunction([true, true, true, true]));
console.log(myFunction(["test", "test", "test"]));
console.log(myFunction([1, 1, 1, 2]));
console.log(myFunction(["10", 10, 10, 10]));

// =====================================================
function myFunction2(arr) {
    return new Set(arr).size === 1;
}

console.log(myFunction2([true, true, true, true]));
console.log(myFunction2(["test", "test", "test"]));
console.log(myFunction2([1, 1, 1, 2]));
console.log(myFunction2(["10", 10, 10, 10]));
