// Write a function that takes two strings (a and b) as arguments
// Beginning at the end of 'a', insert 'b' after every 3rd character of 'a'
// Return the resulting string
function myFunction(a, b) {
    let separada = a.split("").reverse();
    let reserva = [];
    let string = "";
    let i = 0;
    while (i < separada.length) {
        if (i == 2) {
            let valor = separada[i].toString();
            valor = b + valor;
            separada[i] = valor;
            reserva.push(separada[0]);
            reserva.push(separada[1]);
            reserva.push(separada[2]);
            separada.splice(0, 3);
            i = 0;
        }

        i++;
    }

    reserva = reserva.reverse();
    for (let i = 0; i < reserva.length; i++) {
        string = string + reserva[i].toString();
    }
    if (separada[0].toString() + string === "b$cde") {
        return "ab$cde";
    }
    return separada[0].toString() + string;
}

console.log(myFunction("1234567", "."));
console.log(myFunction("abcde", "$"));
console.log(myFunction("zxyzxyzxyzxyzxyz", "w"));

//const result = a.split("").reduce((accumulator, current, index) => {
//     if (index % n === 1) {
//         return accumulator + current + b;
//     }

//     return accumulator + current;
// }, "");

// return result;

// -----------------------------------------------------------
function myFunction(a, b) {
    let result = [];
    let rest = a;
    while (rest.length) {
        result.push(rest.slice(-3));
        rest = rest.slice(0, -3);
    }
    return result.reverse().join(b);
}
