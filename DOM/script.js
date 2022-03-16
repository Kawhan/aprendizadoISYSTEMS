// const heading = document.querySelector("#heading");

// console.log(heading);

const heading = document.getElementById("heading"); // Usado para selecionar a partir do dom o elemento por ID 

// console.log(heading); 
// console.log(typeof heading); // Cada elemento no dom é um objeto, se verificarmos o tipo de dado dessa variável vai ser object

// Como sabemos o id é um tipo de indentificação única mas quando selecionarmos mais de 1 elemento de id, ele sempre vai selecionar apenas o primeiro
// const heading2 = document.getElementById("heading");
// console.log(heading2); 


// const list = document.getElementById("list");

// list.textContent = "Hi There";

// console.log(list.textContent);// define ou retorna o conteúdo textual do Node(nó) especifico e totods os seus elementos(filhos, netos...)

// list.innerHTML = "<h1>Hi there<h1/>"; // Podemos envolver o que esta escrito em texto em tags para criar as tags também, se colocarmos desse modo no textContent ele vai apenas adequart tudo para estilo de texto

// console.log(list.innerHTML); // Define ou retorna o conteúdo HTML de um elemento em outras palavras, ele retorna todo o conteúdo HTML incluindo os atributos de tags e Text Nodes(nó de texto)

const list = document.querySelector("ul");

console.log(list);