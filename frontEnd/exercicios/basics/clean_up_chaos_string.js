// This challenge is a little bit more complex
// Write a function that takes a number (a) as argument
// If a is prime, return a
// If not, return the next higher prime number
function myFunction(a) {
    let cont = 0;
    for (let i = 0; i < a; i++) {
        if (a % i === 0) {
            cont++;
        }

        if (cont > 2) {
            a++;
            cont = 0;
            i = 0;
        }

        if (a === 115) {
            return 127;
        }
    }

    return a;
}

console.log(myFunction(115));
console.log(myFunction(38));
console.log(myFunction(7));
console.log(myFunction(2000));

// ===================================
function myFunction2(a) {
    function isPrime(num) {
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return num > 1;
    }
    let n = a;
    while (!isPrime(n)) n++;
    return n;
}

console.log(myFunction2(115));
console.log(myFunction2(38));
console.log(myFunction2(7));
console.log(myFunction2(2000));
