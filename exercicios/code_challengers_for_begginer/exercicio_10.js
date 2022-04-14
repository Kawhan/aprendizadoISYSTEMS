// 65 97
// 69 101
// 73 105
// 79 111
// 85 117

function contVowels(str) {
    let string = str;
    let cont = 0;

    for (let i = 0; i < string.length; i++) {
        if (
            string.charCodeAt(i) === 65 ||
            string.charCodeAt(i) === 69 ||
            string.charCodeAt(i) === 73 ||
            string.charCodeAt(i) === 79 ||
            string.charCodeAt(i) === 85 ||
            string.charCodeAt(i) === 97 ||
            string.charCodeAt(i) === 101 ||
            string.charCodeAt(i) === 105 ||
            string.charCodeAt(i) === 111 ||
            string.charCodeAt(i) === 117
        ) {
            cont++;
        }
    }

    return cont;
}

console.log(contVowels("Kawhan"));
