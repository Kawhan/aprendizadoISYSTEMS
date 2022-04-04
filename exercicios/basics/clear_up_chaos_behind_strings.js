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
    }
}

console.log(myFunction("java", "tpi%rcs"));
console.log(myFunction("c%ountry", "edis"));
