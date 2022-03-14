const h1 = document.querySelector(".titulo");
const button = document.querySelector("#adicionar-paciente");
h1.textContent = "Aparecida Nutricionista";

const pacientes = document.querySelectorAll(".paciente");

for (let i = 0; i < pacientes.length; i++) {
    const paciente = pacientes[i];

    const tdPeso = paciente.querySelector(".info-peso");
    const peso = tdPeso.textContent;

    const tdAltura = paciente.querySelector(".info-altura");
    const altura = tdAltura.textContent;

    const tdIMC = paciente.querySelector(".info-imc");

    let pesoIsValid = true;
    let alturaIsValid = true;

    if (peso <= 0 || peso >= 1000) {
        console.log("Peso invalido");
        tdIMC.textContent = "Peso invalido";
        pesoIsValid = false;
        paciente.classList.add("paciente-invalido");
    }

    if (altura <= 0 || altura >= 3.0) {
        console.log("Altura invalida");
        tdIMC.textContent = "altura invalida";
        alturaIsValid = false;
        paciente.classList.add("paciente-invalido");
    }

    if (pesoIsValid && alturaIsValid) {
        let imcCalculo = peso / (altura * altura);
        tdIMC.textContent = imcCalculo.toFixed(2);
    }
}

button.addEventListener("click", function (event) {
    event.preventDefault();
    console.log("fui clickado")
});

// Usando forEach para a condição
// pacientes.forEach((paciente) => {
//     const tdPeso = paciente.querySelector(".info-peso");
//     const peso = tdPeso.textContent;

//     const tdAltura = paciente.querySelector(".info-altura");
//     const altura = tdAltura.textContent;

//     const tdIMC = paciente.querySelector(".info-imc");

//     let pesoIsValid = true;
//     let alturaIsValid = true;

//     if (peso <= 0 || peso >= 1000) {
//         console.log("Peso invalido");
//         tdIMC.textContent = "Peso invalido";
//         pesoIsValid = false;
//     }

//     if (altura <= 0 || altura >= 3.0) {
//         console.log("Altura invalida");
//         tdIMC.textContent = "altura invalida";
//         alturaIsValid = false;
//     }

//     if (pesoIsValid && alturaIsValid) {
//         let imcCalculo = peso / (altura * altura);
//         tdIMC.textContent = imcCalculo.toFixed(2);
//     }
// });
