// Return a Boolean if a number is divisible by 10

function divisibleForTen(number) {
    if (number % 10 === 0) {
        return true;
    }

    return false;
}

console.log(divisibleForTen(19));
console.log(divisibleForTen(20));
console.log(divisibleForTen(-10));
console.log(divisibleForTen(10));
console.log(divisibleForTen(100));
console.log(divisibleForTen(20));
console.log(divisibleForTen(22));
console.log(divisibleForTen(12));
