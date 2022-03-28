// const heading = document.querySelector("#heading");

// console.log(heading);

// const heading = document.getElementById("heading"); // Usado para selecionar a partir do dom o elemento por ID

// console.log(heading);
// console.log(typeof heading); // Cada elemento no dom é um objeto, se verificarmos o tipo de dado dessa variável vai ser object

// Como sabemos o id é um tipo de indentificação única mas quando selecionarmos mais de 1 elemento de id, ele sempre vai selecionar apenas o primeiro
// const heading2 = document.getElementById("heading");
// console.log(heading2);

// const list = document.getElementById("list");

// list.textContent = "Hi There";

// console.log(list.textContent);// define ou retorna o conteúdo textual do Node(nó) especifico e totods os seus elementos(filhos, netos...)

// list.innerHTML = "<h1>Hi there<h1/>"; // Podemos envolver o que esta escrito em texto em tags para criar as tags também, se colocarmos desse modo no textContent ele vai apenas adequart tudo para estilo de texto

// console.log(list.innerHTML); // Define ou retorna o conteúdo HTML de um elemento em outras palavras ele retorna todo o conteúdo HTML incluindo os atributos de tags e Text Nodes(nó de texto)

// const list = document.querySelector("ul");
// const list = document.querySelector("#list");
// const list = document.querySelector(".list");

// console.log(list);

// const li = document.querySelector("li");

// console.log(li);

// const lis = document = document.querySelectorAll("li");

// console.log(lis);

// const listItems = document.querySelectorAll(".list-items");

// console.log(listItems);

// const heading =document.getElementById('heading');

// Quando se utiliza className ele substitui a class que tem pela selecionada
// heading.className = "changeBG";
// heading.className = "changeFT";

// Para selecionar mais de uma classe podemos fazer o seguinte, colocar o espaço no inicio DA STRING
// heading.className += " changeFT";

// console.log(heading)

// ClassList
// heading.classList.add("changeCL");
// heading.classList.remove("changeCL");

// console.log(heading.classList);

// heading.style.color = 'red';
// heading.style.backgroundColor = "black";

// const lis = document = document.querySelectorAll("li");

// lis[0].style.backgroundColor = "red";

// for(let i = 0; i < lis.length; i++) {
//     lis[i].style.backgroundColor = "royalblue";
// }

// lis[0].style.cssText = "background-color: coral; color: white; font-size: 25px";

// const heading = document.querySelector(".heading");
// const btn = document.querySelector(".btn");

// Click no botão
// btn.onclick = () => {
//     console.log("click");
// };

// Mouse perto do componente
// btn.onmouseover = () => {
//     heading.style.cssText = 'background-color: brown; color: white';
// };

// Mouse fora do componente
// btn.onmouseout = () => {
//     heading.style.cssText = 'background-color: trasparent; color: black';
// };

// const clickButton = () => {
//     console.log("clicked!");
// };

// btn.addEventListener("click", (event) => {
// heading.style.cssText = "background-color: brown; color: white";
//     console.log(event.target);
// })

// const paragraph = document.querySelector('.paragraph');
// console.log(paragraph.getAttribute("id"));
// console.log(paragraph.getAttribute("class"));
// console.log(paragraph.getAttribute("title")); // retorna null

// Adicionar um valor de atributo para a saída especificada se o valor existir é atualizado caso contrario ele é criado
// paragraph.setAttribute('style', 'background-color: coral');
// Remover o atributo
// paragraph.removeAttribute('style');

// Checar se tem um atributo style
// console.log(paragraph.hasAttribute("style"));

const listItem = document.getElementById("list-item");
// Laço para mostra o pai, usando essa propriedade também podemos acessas os avos usando mais de uma vez
// console.log(listItem.parentNode);
// console.log(listItem.parentElement);
// console.log(listItem.parentNode.parentNode);

const list = document.querySelector(".list");
// Vai retornar os elementos até mesmo os espaços de texto ou espaços normais
// console.log(list.childNodes);
// Para não retornar o texto usamos
// console.log(list.children);
// Primeiro elemento filho de nossa lista
// console.log(list.firstElementChild);

// Pega espaços em brancos assosiados como irmãos
// console.log(listItem.previousSibling);
// Pega somente elementos
// console.log(listItem.previousElementSibling);
// console.log(list.previousElementSibling);
// console.log(list.nextElementSibling);

// Criar um elemento nos utilizamos o create element
const newEl = document.createElement("li");

// Criar elementos de texto
const text = document.createTextNode("Blog");

// Permitir que coloquemos elementos dentro de outros
newEl.appendChild(text);

console.log(newEl);

// Por comportamento padrão ele coloca sempre no final se quisermos mudar de posição temos de colocar o insertBefore
// list.appendChild(newEl);
// elemento    posição
list.insertBefore(newEl, list.children[0]);

// remover os elementos
list.removeChild(newEl);

// console.log(text);
// console.log(newEl);
