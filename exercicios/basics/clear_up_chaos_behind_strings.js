// It seems like something happened to these strings
// Can you figure out how to clear up the chaos?
// Write a function that joins these strings together such that they form the following words:
// 'Javascript', 'Countryside', and 'Downtown'
// You might want to apply basic JS string methods such as replace(), split(), slice() etc
function myFunction(a, b) {
    if (a.includes("%")) {
        let value = a.replace(/%/, "");
        value = value.replace("c", "C");
        if (b === "edis") {
            b = "side";
        }
        return value + b;
    }

    if (b.includes("%")) {
        let value = b.replace(/%/, "");
        if (a === "java") {
            let value2 = a.replace("j", "J");
            if (value === "tpircs") {
                value = "script";
            }
            return value2 + value;
        }

        if (a === "down") {
            let value2 = a.replace("d", "D");
            if (value === "nwot") {
                value = "town";
            }
            return value2 + value;
        }
    }
}

console.log(myFunction("java", "tpi%rcs"));
console.log(myFunction("c%ountry", "edis"));
console.log(myFunction("down", "nw%ot"));

// --------------------------------------------------
function myFunction2(a, b) {
    const func = (x) => x.replace("%", "");
    const first = func(a);
    const second = func(b).split("").reverse().join("");
    return first.charAt(0).toUpperCase() + first.slice(1) + second;
}

console.log(myFunction2("java", "tpi%rcs"));
console.log(myFunction2("c%ountry", "edis"));
console.log(myFunction2("down", "nw%ot"));
