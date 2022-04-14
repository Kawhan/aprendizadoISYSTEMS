const pacientes_num = document.querySelectorAll(".paciente");

var tabela = document.querySelector('#tabela-pacientes');

// Clicando 2 vezes na nossa tabela ele seleciona esse evento
tabela.addEventListener('dblclick', function(event) {

    event.target.parentNode.classList.add("fadeOut");

    setTimeout(function () {
        // Somente executará nosso código caso o elemento em que clicamos seja um <td>
        if (event.target.tagName == 'TD') {
            event.target.parentNode.remove();
        }
    }, 500);
});


// const tabela = document.querySelector("table");

// tabela.addEventListener("dblclick", function (event) {
//     const alvoEvento = event.target; 
//     const paiDoEvento = alvoEvento.parentNode; // TR
    
//     event.target.parentNode.classList.add("fadeOut");

//     setTimeout(function () {
//         Somente executará nosso código caso o elemento em que clicamos seja um <td>
//         if (event.target.tagName == 'TD') {
//             event.target.parentNode.remove();
//         }
//     }, 500);

   
// });

// pacientes_num.forEach(paciente => {
//     paciente.addEventListener("dblclick", function () {
//         this.remove();
//     })
// })