const pacientes_num = document.querySelectorAll(".paciente");

const tabela = document.querySelector("table");

tabela.addEventListener("dblclick", function (event) {
    const alvoEvento = event.target; 
    const paiDoEvento = alvoEvento.parentNode; // TR

    paiDoEvento.remove();
});

// pacientes_num.forEach(paciente => {
//     paciente.addEventListener("dblclick", function () {
//         this.remove();
//     })
// })