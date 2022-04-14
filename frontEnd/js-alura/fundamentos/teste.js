function myFunction(a , n) {
    let w_string = "";

    if (n == 0 || n == 1) {
        w_string = a[0];
    }
    else {
        w_string = a[n - 1];
    }

    return w_string;
}

console.log(myFunction('abcd', 1));
console.log(myFunction('zyxbwpl',5));
console.log(myFunction('gfedcba',3));

function myFunction2(a){
    return a.slice(3)
}

console.log(myFunction2('abcdefg'))

function myFunction3(a, b){
    return (a / 100) * b;
}

console.log(myFunction3(100,50));
console.log(myFunction3(10,1));
console.log(myFunction3(500,25));

// function myFunction(a, b) {
//     return b.split(a).length - 1
// }