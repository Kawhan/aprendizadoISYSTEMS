// Remove the spaces found in a string
// &nbsp
function removeSpace(arr) {
    let strings = arr;
    let aux = [];
    let value;

    strings.forEach((element) => {
        for (let i = 0; i < element.length; i++) {
            value = element.charCodeAt(i);
            if (value == 32) {
                element = element.replace(/\s/g, "");
            }
        }
        aux.push(element);
    });

    return aux;
}

console.log(removeSpace(["Ka wh a n ", "O la", "T i me"]));
