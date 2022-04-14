// Create a function that filters out negative numbers

function filterNegative(arr) {
    let array_correct = [];

    arr.forEach((element) => {
        if (element >= 0) {
            array_correct.push(element);
        }
    });

    return array_correct;
}

console.log(filterNegative([-1, -2, -3, 4, -11]));
