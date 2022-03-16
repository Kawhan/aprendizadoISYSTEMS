const campoFiltro = document.querySelector("#filtrar-tabela"); // Selecionando nossa tabela

campoFiltro.addEventListener("input" , function () {
    campoFiltro.value;
    // Selecionando todos os pacientes, tr com class pacientes
    const pacientes_nomes = document.querySelectorAll(".paciente");

    if (this.value.length > 0) {
        pacientes_nomes.forEach(paciente => {

            // Selecionando em nosso tr nosso td
            const tdNome = paciente.querySelector(".info-nome");
            // Selecionando o que tem dentro do nosso td
            const nome = tdNome.textContent;
    
            // Expressão regular para ir comparando nosso campoFiltro, sem case sensitive
            const expressao = new RegExp(this.value, "i");

            // Comparação usando test e nosso nome pegado do tdNome
            if( !expressao.test(nome)) {
                paciente.classList.add("invisivel");
    
            }else {
                paciente.classList.remove("invisivel");
            }
        });
    } else {
        pacientes_nomes.forEach(paciente => {
            paciente.classList.remove("invisivel");
        });
    }
    
});