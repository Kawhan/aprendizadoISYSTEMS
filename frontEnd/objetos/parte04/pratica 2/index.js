let myObj = { name: "Chris", age: 38 };
console.log(myObj);
let myString = JSON.stringify(myObj);
console.log(myString);

async function populate() {
    const requestURL =
        "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
    const request = new Request(requestURL);

    const response = await fetch(request);
    const superHeroesText = await response.text();

    console.log(response);
    console.log(superHeroesText);
    const superHeroes = JSON.parse(superHeroesText);
}

populate();
